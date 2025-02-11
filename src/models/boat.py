class Boat:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = 0

    def add_passenger(self):
        if self.passengers < self.capacity:
            self.passengers += 1
        else:
            raise ValueError("Лодка заполнена")

    def remove_passenger(self):
        if self.passengers > 0:
            self.passengers -= 1
        else:
            raise ValueError("Лодка пуста")
