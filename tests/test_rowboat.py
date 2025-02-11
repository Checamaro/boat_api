import pytest
import allure
from src.models.rowboat import Rowboat

@allure.feature("Инициализация лодки")
def test_boat_initialization():
    boat = Rowboat(2)
    assert boat.capacity == 2
    assert boat.passengers == 0

@allure.feature("Управление пассажирами")
def test_add_passenger():
    boat = Rowboat(2)
    boat.add_passenger()
    assert boat.passengers == 1

@allure.feature("Перемещение лодки")
def test_movement():
    boat = Rowboat(2)
    boat.move()
    assert boat.position == (0, 1)

@allure.feature("Смена направления")
@pytest.mark.parametrize("direction", ["north", "south", "east", "west"])
def test_change_direction(direction):
    boat = Rowboat(2)
    boat.change_direction(direction)
    assert boat.direction == direction

@allure.feature("Остановка лодки")
def test_stop():
    boat = Rowboat(2)
    boat.stop()
