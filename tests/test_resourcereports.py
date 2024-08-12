import os
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.PMOIcon import PMOIcon
from pageObjects.ResourceReports import ResourceReports
from utilities.BaseClass import BaseClass, read_excel, get_web_data, compare_data
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TestTwo(BaseClass):

    def test_resourceReports(self):
        wait = WebDriverWait(self.driver, 10)
        pmoIcon = PMOIcon(self.driver)
        pmoIcon.PmIcon().click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("undefined")
        time.sleep(3)
        self.driver.implicitly_wait(15)
        resReport = ResourceReports(self.driver)
        resReport.ResReport().click()
        to_date = wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         "//mat-datepicker-toggle[@class='mat-datepicker-toggle ng-tns-c53-1']//span[@class='mat-button-wrapper']//*[name()='svg']"))

        )
        to_date.click()
        date_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='August 15, 2024']")))
        date_to_select.click()
        time.sleep(3)
        expoReport = ResourceReports(self.driver)
        expoReport.ExpoReport().click()
        time.sleep(3)
        download_dir = r"C:\Users\Anupama Saranu\PycharmProjects\PythonSelFramework"
        file_name = "Project Resource Reports.xlsx"
        file_path = os.path.join(download_dir, file_name)
        body = self.driver.find_element(By.XPATH, "//body")
        action = ActionChains(self.driver)
        action.move_to_element(body).click().perform()

        # Read data from the file
        file_data = read_excel(file_path)
        print(file_data)

        # Get data from the web application
        web_data = get_web_data(self.driver)

        # Compare data
        compare_data(file_data, web_data)