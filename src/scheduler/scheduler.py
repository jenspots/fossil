import docker
import schedule
import time

from src.task import Task
from loguru import logger


class Scheduler:
    tasks: list[Task]

    filters = {
        "label": ["fossil.enable=true"],
        "status": "running",
    }

    def __init__(self):
        self.client = docker.from_env()
        containers = self.client.containers.list(filters=self.filters)

        # Announce the found containers
        logger.info(f"Found {len(containers)} containers")

        # Keep reference to tasks
        self.tasks = list(map(Task.from_container, containers))

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
