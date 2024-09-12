import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

class home_page:
    def __init__(self, driver):
        #save driver
        self.driver = driver


    def locators(self):
        time.sleep(5)
        acceptBtn = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Accept')]")

    def testCreateNewPlate(self):
        time.sleep(5)
        #homePage = home_page(self)
        #homePage.locators()
        acceptBtn = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Accept')]")
        newBtn = self.driver.find_element(By.ID, "addNewBtn")
        # home_page.locators().acceptBtn.click()
        acceptBtn.click()
        time.sleep(5)
        newBtn.click()
        time.sleep(5)
        addNewPlate = self.driver.find_element(By.ID, "appNewFileLinkPlateSetup")
        addNewPlate.click()
        #assert "Plate Setup" in self.driver.c
        time.sleep(5)
