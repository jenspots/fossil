import sched
from threading import Thread

import docker
import time

from docker import DockerClient
from src.task import Task
from loguru import logger


class Scheduler:
    client: DockerClient
    scheduler: sched.scheduler
    scheduled: dict[Task, sched.Event]

    filters = {
        "label": ["fossil.enable=true"],
        "status": "running",
    }

    def __init__(self):
        # Docker information
        self.client = docker.from_env()
        containers = self.client.containers.list(filters=self.filters)

        # Announce the found containers
        logger.info(f"Found {len(containers)} containers")

        # The scheduler itself
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.scheduled = dict()

        # Keep reference to tasks
        for container in containers:
            task = Task.from_container(container)
            event = self.scheduler.enter(1, 0, self.execute, argument=tuple([task]))
            self.scheduled[task] = event

        # Listen to the Docker socket for changes
        Thread(target=self.events).start()

    def execute(self, task: Task):
        # Pop the event
        _ = self.scheduled.pop(task)

        # Run the task
        task.run()

        # Schedule it for later
        event = self.scheduler.enter(1, 0, self.execute, argument=tuple([task]))
        self.scheduled[task] = event

    def events(self):
        for event in self.client.events(filters=self.filters, decode=True):
            if event["Action"] in ["start", "stop"]:
                logger.info(event)

    def run(self):
        self.scheduler.run()
