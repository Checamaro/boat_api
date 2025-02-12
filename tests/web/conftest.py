import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
