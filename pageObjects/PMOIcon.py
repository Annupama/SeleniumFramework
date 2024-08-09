from selenium.webdriver.common.by import By


class PMOIcon:

    def __init__(self,driver):
        self.driver = driver
    # this is the tuple
    pmIcon = (By.CSS_SELECTOR, "img[alt='Project Management']")

    def PmIcon(self):
        return self.driver.find_element(*PMOIcon.pmIcon)   # If we use star, it will reads the particular variables as tuple and will de_serialised

