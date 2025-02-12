from .boat import Boat
from src.utils.helpers import validate_direction


class Rowboat(Boat):
    def __init__(self, name: str, capacity: int, oars: int):
        super().__init__(name, capacity)
        self.oars = oars

    def move(self, direction: str):
        if not validate_direction(direction):
            raise ValueError("Invalid direction")
        super().move(direction)
