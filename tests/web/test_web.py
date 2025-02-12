import time
import allure
from selenium.webdriver.common.by import By

@allure.feature("Web: Контроль лодки через UI")
@allure.story("Перемещение лодки")
def test_web_controls(browser):
    with allure.step("Открытие веб-приложения"):
        browser.get("http://127.0.0.1:8001")
        time.sleep(2)

    with allure.step("Нажатие на кнопку 'Move Forward'"):
        move_forward = browser.find_element(By.XPATH, "//button[text()='Move Forward']")
        move_forward.click()
        time.sleep(2)

    with allure.step("Нажатие на кнопку 'Stop'"):
        stop_button = browser.find_element(By.XPATH, "//button[text()='Stop']")
        stop_button.click()
        time.sleep(2)

    with allure.step("Закрытие браузера"):
        pass