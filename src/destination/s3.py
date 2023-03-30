from src.destination.destination import Destination


class S3(Destination):
    def write(self, data: bytearray):
        NotImplementedError()
