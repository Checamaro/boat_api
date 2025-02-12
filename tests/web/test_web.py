import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Web: Контроль лодки через UI")
@allure.story("Перемещение лодки")
def test_web_controls(browser):
    wait = WebDriverWait(browser, 10)
    short_wait = WebDriverWait(browser, 3)

    with allure.step("Открытие веб-приложения"):
        browser.get("http://127.0.0.1:8001")

    with allure.step("Добавление двух пассажиров"):
        add_passenger_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Passenger']")))
        for _ in range(2):
            add_passenger_button.click()
            short_wait.until(lambda driver: int(driver.find_element(By.ID, "passengerCount").text) >= (_ + 1))

    with allure.step("Перемещение лодки по периметру"):
        move_forward = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Move Forward']")))
        move_right = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Move Right']")))
        move_backward = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Move Backward']")))
        move_left = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Move Left']")))
        stop_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Stop']")))

        def move_steps(button, direction, steps=10):
            """Двигает лодку несколько шагов в заданном направлении с паузами."""
            for _ in range(steps):
                button.click()
                short_wait.until(EC.text_to_be_present_in_element((By.ID, "boatDirection"), direction))
            stop_button.click()
            short_wait.until(EC.text_to_be_present_in_element((By.ID, "boatDirection"), "Остановлено"))

        move_steps(move_forward, "forward", steps=10)
        move_steps(move_right, "right", steps=15)
        move_steps(move_backward, "backward", steps=10)
        move_steps(move_left, "left", steps=15)

    with allure.step("Закрытие браузера"):
        pass

