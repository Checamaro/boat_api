import requests
import allure

BASE_URL = "http://127.0.0.1:8000"


@allure.feature("API: Управление лодкой")
@allure.story("Перемещение лодки")
def test_move():
    with allure.step("Отправка запроса на перемещение лодки вперед"):
        response = requests.post(f"{BASE_URL}/move/forward")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200
        assert response.json()["message"] == "Boat moved forward"


@allure.feature("API: Управление лодкой")
@allure.story("Остановка лодки")
def test_stop():
    with allure.step("Отправка запроса на остановку лодки"):
        response = requests.post(f"{BASE_URL}/stop")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200
        assert response.json()["message"] == "Boat stopped"


@allure.feature("API: Управление пассажирами")
@allure.story("Добавление пассажира")
def test_add_passenger():
    with allure.step("Отправка запроса на добавление пассажира"):
        response = requests.post(f"{BASE_URL}/passenger/add")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200


@allure.feature("API: Управление пассажирами")
@allure.story("Удаление пассажира")
def test_remove_passenger():
    with allure.step("Отправка запроса на удаление пассажира"):
        response = requests.post(f"{BASE_URL}/passenger/remove")

    with allure.step("Проверка ответа API"):
        assert response.status_code == 200
