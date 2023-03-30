import os
from datetime import datetime
from src.destination.destination import Destination


class Local(Destination):
    directory: str

    def __init__(self, directory: str):
        self.directory = f"{os.getenv('OUTPUT_DIRECTORY')}{directory}"

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def write(self, data: bytearray):
        path = f"{self.directory}{datetime.now().isoformat().replace(':', '')}.txt"
        file = open(path, mode="xb")
        file.write(data)
        file.close()
