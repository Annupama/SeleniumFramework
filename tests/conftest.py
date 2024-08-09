import time

from selenium.webdriver.chrome.options import Options
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
        chrome_options = Options()
        download_dir = r"C:\Users\Anupama Saranu\PycharmProjects\PythonSelFramework"

        # Set Chrome preferences
        chrome_prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)

        # Initialize Chrome WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
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
