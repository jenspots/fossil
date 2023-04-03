from . import Task
from loguru import logger


class Command(Task):
    command = "pg_dump gsr -U gsr"

    def run(self):
        logger.info(f"{self.name}")
        result = self.container.exec_run(self.command)
        self.destination.write(result.output)
