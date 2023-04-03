import os
from datetime import datetime
from . import Destination


class Local(Destination):
    directory: str
    path: str

    def __init__(self, directory: str, path: str):
        self.directory = os.getenv("OUTPUT_DIRECTORY") + "/" + directory
        self.path = path

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def write(self, data: bytearray):
        # Generate the file path
        timestamp = datetime.now().isoformat().replace(":", "")
        path = self.path.replace("<DATETIME>", timestamp)

        # Write to disk
        file = open(self.directory + "/" + path, mode="xb")
        file.write(data)
        file.close()
