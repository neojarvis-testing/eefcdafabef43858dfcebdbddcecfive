from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

class WebDriverHelper:
    def __init__(self, driver):
        self.driver = driver

    def openPage(self, url):
        try:
            self.driver.get(url)
        except WebDriverException as e:
            e.printStackTrace()
            raise Exception("Error in " + str(e))

    def clickElement(self, locator):
        try:
            element = self.driver.find_element(*locator)
            element.click()
        except WebDriverException as e:
            print(e)
            raise Exception("Error in " + str(e))


    def fillForm(self, locator, text):
        try:
            element = self.driver.find_element(*locator)  
            element.send_keys(text)
        except WebDriverException as e:
            traceback.print_exc()  
            raise Exception("Error in " + str(e))
        
    def hoverOneElement(self, locator):
        try:
            element = self.driver.find_element(locator)
            Actions(self.driver).move_to_element(element).perform()
        except WebDriverException as e:
            e.printStackTrace()
            raise Exception("Error in " + str(e))

    def hoverTwoElements(self, firstLocator, secondLocator):
        try:
            firstElement = self.driver.find_element(firstLocator)
            secondElement = self.driver.find_element(secondLocator)
            
            actions = Actions(self.driver)
            actions.move_to_element(firstElement).move_to_element(secondElement).perform()
        except WebDriverException as e:
            e.printStackTrace()
            raise Exception("Error in " + str(e))
