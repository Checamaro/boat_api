import pytest
import allure
import requests

BASE_URL = "http://127.0.0.1:8000"

@allure.feature("API Доступность")
def test_api_running():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json()["message"] == "Boat API is running!"

@allure.feature("Получение состояния лодки")
def test_get_boat_status():
    response = requests.get(f"{BASE_URL}/boat")
    assert response.status_code == 200
    data = response.json()
    assert "capacity" in data
    assert "passengers" in data
    assert "position" in data
    assert "direction" in data

@allure.feature("Добавление пассажира")
def test_add_passenger():
    response = requests.post(f"{BASE_URL}/boat/passenger")
    assert response.status_code == 200
    assert response.json()["message"] == "Passenger added"

@allure.feature("Удаление пассажира")
def test_remove_passenger():
    response = requests.delete(f"{BASE_URL}/boat/passenger")
    assert response.status_code == 200
    assert response.json()["message"] == "Passenger removed"

@allure.feature("Изменение направления лодки")
@pytest.mark.parametrize("direction", ["north", "south", "east", "west"])
def test_change_direction(direction):
    response = requests.put(f"{BASE_URL}/boat/direction/{direction}")
    assert response.status_code == 200
    assert response.json()["message"] == f"Direction changed to {direction}"

@allure.feature("Движение лодки")
def test_move_boat():
    response = requests.put(f"{BASE_URL}/boat/move")
    assert response.status_code == 200
    assert "position" in response.json()

@allure.feature("Остановка лодки")
def test_stop_boat():
    response = requests.put(f"{BASE_URL}/boat/stop")
    assert response.status_code == 200
    assert response.json()["message"] == "Boat stopped"
