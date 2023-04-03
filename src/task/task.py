import schedule
from loguru import logger

from src.destination import Destination


class Task:
    name: str
    destination: Destination

    def __init__(self, container, destination: Destination):
        self.destination = destination
        self.name = container.name
        self.container = container

    @staticmethod
    def from_container(container) -> "Task":
        from src.task.command import Command

        logger.info(f"New container: {container.name}")

        destination = Destination.from_container(container)
        task = Command(container, destination)
        schedule.every(5).seconds.do(task.run)
        return task

    def run(self):
        NotImplementedError()
