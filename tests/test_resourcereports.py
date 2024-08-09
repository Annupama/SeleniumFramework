import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.PMOIcon import PMOIcon
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TestTwo(BaseClass):

    def test_resourcereports(self):
        wait = WebDriverWait(self.driver, 10)
        pmoIcon = PMOIcon(self.driver)
        pmoIcon.PmIcon().click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("undefined")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//a[@id='ngb-nav-4']").click()
        to_date = wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         "//mat-datepicker-toggle[@class='mat-datepicker-toggle ng-tns-c53-1']//span[@class='mat-button-wrapper']//*[name()='svg']"))

        )
        to_date.click()
        date_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='August 9, 2024']")))
        date_to_select.click()
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Export Reports']").click()