class Destination:
    def write(self, data: bytearray):
        NotImplementedError()

    @staticmethod
    def from_container(container) -> "Destination":
        from src.destination.local import Local

        path = container.labels["fossil.dump.destination.local"]
        return Local(container.name, path)
