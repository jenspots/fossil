class Destination:
    def write(self, data: bytearray):
        NotImplementedError()

    @staticmethod
    def from_container(container) -> "Destination":
        from src.destination.local import Local

        return Local(directory=f"{container.name}/")
