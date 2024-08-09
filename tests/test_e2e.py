import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.PMOIcon import PMOIcon
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TestOne(BaseClass):

    def test_e2e(self):
        wait = WebDriverWait(self.driver, 10)
        pmoIcon = PMOIcon(self.driver)
        pmoIcon.PmIcon().click()
        time.sleep(3)
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("undefined")
        self.driver.implicitly_wait(5)
# Adding new client
        self.driver.find_element(By.XPATH,"//img[@title='Client Configuration']").click()
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Add Client']").click()
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter Client Name']").send_keys("Test Client789")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Select Region']").send_keys("west")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Select Country']").send_keys("United States")
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Address']").send_keys("Test Address")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter City']").send_keys("Test City")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter State']").send_keys("Test State")
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='clientBillingType']"))
        dropdown.select_by_value("1")
        add = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        add.click()
# Assigning new client that created above to the new project
        self.driver.find_element(By.XPATH, "//img[@title='Project Configuration']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Project']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Test Client789")
        action = ActionChains(self.driver)
        body1 = self.driver.find_element(By.XPATH, "//body")
        action.move_to_element(body1).click().perform()
        projectname = (self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Project Name']"))
        projectname.send_keys("Test Automate")
        test_description = (self.driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Description']"))
        test_description.send_keys("Test")
        notes = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Notes']")
        notes.send_keys("Testing")
        email = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
        email.send_keys("test4.automation@cognine.com")
        body1 = self.driver.find_element(By.XPATH, "//body")
        action.move_to_element(body1).click().perform()
        dropdown_element = self.driver.find_element(By.XPATH,
                                                    "//span[contains(@class, 'ng-star-inserted') and text()='Select Technologies']")
        dropdown_element.click()
        technologies = [".Net", "Angular"]
        for option in technologies:
            label = self.driver.find_element(By.XPATH,
                                             "//label[contains(@class, 'ng-star-inserted') and text()='{}']".format(
                                                 option))
            label.click()
        body = self.driver.find_element(By.XPATH, "//body")
        action.move_to_element(body).click().perform()
        # Start Date
        start_date = wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         "//mat-datepicker-toggle[@class ='mat-datepicker-toggle ng-tns-c53-1']//span[@class='mat-button-wrapper']//*[name()='svg']"))

        )
        start_date.click()
        date_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='August 15, 2024']")))
        date_to_select.click()
        add = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        add.click()



