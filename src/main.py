import docker
from dotenv import load_dotenv
import time
import schedule
from src.task import Task


if __name__ == "__main__":
    load_dotenv()
    client = docker.from_env()

    for container in client.containers.list(filters={"name": "website-postgres"}):
        Task.from_container(container)

    while True:
        schedule.run_pending()
        time.sleep(1)
