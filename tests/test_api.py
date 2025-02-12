import pytest
import allure
import requests

BASE_URL = "http://127.0.0.1:8000"

@allure.feature("API Доступность")
@allure.story("Проверка доступности API")
def test_api_running():
    with allure.step("Отправка запроса на корневой маршрут API"):
        response = requests.get(f"{BASE_URL}/")

    with allure.step("Проверка кода ответа и сообщения"):
        assert response.status_code == 200, "API недоступен"
        assert response.json()["message"] == "Boat API is running!"


@allure.feature("Получение состояния лодки")
@allure.story("Запрос текущего состояния лодки")
def test_get_boat_status():
    with allure.step("Отправка запроса на получение состояния лодки"):
        response = requests.get(f"{BASE_URL}/boat")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200, "Ошибка получения состояния лодки"
        data = response.json()
        assert "capacity" in data, "Отсутствует информация о вместимости"
        assert "passengers" in data, "Отсутствует информация о пассажирах"
        assert "position" in data, "Отсутствует информация о положении"
        assert "direction" in data, "Отсутствует информация о направлении"


@allure.feature("Управление пассажирами")
@allure.story("Добавление пассажира")
def test_add_passenger():
    with allure.step("Отправка запроса на добавление пассажира"):
        response = requests.post(f"{BASE_URL}/boat/passenger")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200, "Ошибка добавления пассажира"
        assert response.json()["message"] == "Passenger added"


@allure.feature("Управление пассажирами")
@allure.story("Удаление пассажира")
def test_remove_passenger():
    with allure.step("Отправка запроса на удаление пассажира"):
        response = requests.delete(f"{BASE_URL}/boat/passenger")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200, "Ошибка удаления пассажира"
        assert response.json()["message"] == "Passenger removed"


@allure.feature("Изменение направления лодки")
@allure.story("Изменение направления движения")
@pytest.mark.parametrize("direction", ["north", "south", "east", "west"])
def test_change_direction(direction):
    with allure.step(f"Отправка запроса на смену направления на {direction}"):
        response = requests.put(f"{BASE_URL}/boat/direction/{direction}")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200, "Ошибка смены направления"
        assert response.json()["message"] == f"Direction changed to {direction}"


@allure.feature("Движение лодки")
@allure.story("Перемещение лодки вперёд")
def test_move_boat():
    with allure.step("Отправка запроса на движение лодки"):
        response = requests.put(f"{BASE_URL}/boat/move")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200, "Ошибка движения лодки"
        assert "position" in response.json(), "Отсутствует информация о положении лодки"


@allure.feature("Движение лодки")
@allure.story("Остановка лодки")
def test_stop_boat():
    with allure.step("Отправка запроса на остановку лодки"):
        response = requests.put(f"{BASE_URL}/boat/stop")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200, "Ошибка остановки лодки"
        assert response.json()["message"] == "Boat stopped"