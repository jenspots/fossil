from . import Task
from loguru import logger
from docker.models.containers import Container

from ..destination import Destination


class Command(Task):
    command: str

    def __init__(self, container: Container, destination: Destination):
        super().__init__(container, destination)
        self.command = container.labels["fossil.dump.command"]

    def run(self):
        logger.info(f"{self.name}")
        result = self.container.exec_run(self.command)
        self.destination.write(result.output)
