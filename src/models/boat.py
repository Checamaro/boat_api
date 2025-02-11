from abc import ABC, abstractmethod

class Boat(ABC):
    def __init__(self, capacity: int, material: str):
        self.capacity = capacity
        self.passengers = 0
        self.material = material
        self.position = (0, 0)
        self.direction = "north"
        self._is_moving = False

    @abstractmethod
    def move(self):
        pass

    def add_passenger(self):
        if self.passengers >= self.capacity:
            raise ValueError("Достигнута максимальная вместимость")
        self.passengers += 1

    def remove_passenger(self):
        if self.passengers <= 0:
            raise ValueError("Нет пассажиров для удаления")
        self.passengers -= 1

    def change_direction(self, new_direction: str):
        valid_directions = {"north", "south", "east", "west"}
        if new_direction.lower() not in valid_directions:
            raise ValueError("Некорректное направление")
        self.direction = new_direction.lower()

    def stop(self):
        self._is_moving = False

    @property
    def is_moving(self):
        return self._is_moving
