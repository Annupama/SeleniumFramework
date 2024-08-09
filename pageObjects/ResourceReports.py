from selenium.webdriver.common.by import By


class ResourceReports:

    def __init__(self,driver):
        self.driver = driver
    # this is the tuple
    resReport = (By.XPATH, "//a[@id='ngb-nav-4']")
    expoReport = (By.XPATH,"//button[normalize-space()='Export Reports']")

    def ResReport(self):
        return self.driver.find_element(*ResourceReports.resReport) # If we use star, it will reads the particular variables as tuple and will de_serialised

    def ExpoReport(self):
        return self.driver.find_element(*ResourceReports.expoReport)
