from .boat import Boat

class Rowboat(Boat):
    def __init__(self, capacity: int, material: str):
        super().__init__(capacity, material)
        self._stroke_count = 0

    def move(self):
        self._is_moving = True
        self._update_position()
        self._stroke_count += 1

    def _update_position(self):
        movement = {
            "north": (0, 1),
            "south": (0, -1),
            "east": (1, 0),
            "west": (-1, 0)
        }
        dx, dy = movement[self.direction]
        self.position = (self.position[0] + dx, self.position[1] + dy)
