from .boat import Boat

class Rowboat(Boat):
    def __init__(self, name: str, capacity: int, oars: int):
        super().__init__(name, capacity)
        self.oars = oars

    def move(self, direction: str):
        if direction in ["forward", "backward", "left", "right"]:
            self.direction = direction
        else:
            raise ValueError("Invalid direction")
