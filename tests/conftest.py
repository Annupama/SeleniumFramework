import time

from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "IE":
        driver = webdriver.Edge()

    wait = WebDriverWait(driver, 10)
    driver.get("https://chorusqa.cogninelabs.com/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("chorus.automation@cognine.com")
    driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Welcome2Cognine")
    driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
    driver.implicitly_wait(20)

    request.cls.driver = driver
    yield
    driver.close()
