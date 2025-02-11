from src.models.boat import Boat
import logging

logger = logging.getLogger(__name__)

class Rowboat(Boat):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.position = (0, 0)
        self.direction = "north"

    def move(self):
        logger.info(f"Лодка движется на {self.direction}")
        x, y = self.position
        if self.direction == "north":
            self.position = (x, y + 1)
        elif self.direction == "south":
            self.position = (x, y - 1)
        elif self.direction == "east":
            self.position = (x + 1, y)
        elif self.direction == "west":
            self.position = (x - 1, y)

    def change_direction(self, new_direction):
        if new_direction in ["north", "south", "east", "west"]:
            self.direction = new_direction
            logger.info(f"Направление изменено на {new_direction}")
        else:
            raise ValueError("Некорректное направление")

    def stop(self):
        logger.info("Лодка остановилась")
