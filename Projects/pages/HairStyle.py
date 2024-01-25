import logging
import time
import allure  
from selenium.webdriver.common.by import By
from utilities.screenshot import Screenshot
from locaters.uiHairStyle import HairstyleUI
from utilities.webDriverHelper import WebDriverHelper

class HairStylePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on Styles")
    def click_styles(self):
        try:
            logging.info("Scrolling down and clicking on Styles.")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            locator = (By.XPATH, HairstyleUI.click_style)
            WebDriverHelper(self.driver).clickElement(locator)
            logging.info("Clicked on Styles successfully.")
        except Exception as e:
            logging.error(f"Error while clicking on Styles: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click on Facial")
    def click_facial(self):
        try:
            logging.info("Clicking on Facial.")
            time.sleep(5)
            locator = (By.XPATH, HairstyleUI.click_facial)
            WebDriverHelper(self.driver).clickElement(locator)
            logging.info("Clicked on Facial successfully.")
        except Exception as e:
            logging.error(f"Error while clicking on Facial: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
