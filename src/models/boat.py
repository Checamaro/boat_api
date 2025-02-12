class Boat:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.passengers = 0
        self.direction = "stopped"

    def move(self, direction: str):
        if direction in ["left", "right", "forward", "backward"]:
            self.direction = direction
        else:
            raise ValueError("Invalid direction")

    def stop(self):
        self.direction = "stopped"

    def add_passenger(self):
        if self.passengers < self.capacity:
            self.passengers += 1
        else:
            raise ValueError("Boat is full")

    def remove_passenger(self):
        if self.passengers > 0:
            self.passengers -= 1
        else:
            raise ValueError("No passengers to remove")
