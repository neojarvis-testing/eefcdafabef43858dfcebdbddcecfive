import logging
import time
import allure  
from selenium.webdriver.common.by import By
from utilities.excelReader import ExcelReader  
from locaters.uiRazor import RazorUI
from utilities.screenshot import Screenshot
from utilities.webDriverHelper import WebDriverHelper

class GillettePage:
    def __init__(self, driver):
        self.driver = driver
        self.excel_reader = ExcelReader('/Users/tamil/Desktop/PythonSeleniumDemo/Projects/data/Datasheet.xlsx')  
        self.search_queries = self.get_search_queries()  

    def get_search_queries(self):
        data = self.excel_reader.get_data(sheet_name='Sheet1')  
        return [row['Keys'] for row in data] 


    @allure.step("Click on search box")
    def click_search_box(self):
        try:
            locator = (By.XPATH, RazorUI.search_icon)
            WebDriverHelper(self.driver).clickElement(locator)
            logging.info("Clicked on Search icon successfully.")

            assert WebDriverHelper(self.driver).isElementPresent(locator), "Search icon not clicked"
            return True
        except Exception as e:
            logging.error(f"Error while clicking on search icon: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            return False

    @allure.step("Enter search query")
    def enter_search_query(self):
        try:
            locator = (By.XPATH, RazorUI.search_box)
            for query in self.search_queries:  
                WebDriverHelper(self.driver).fillForm(locator, query)  
                time.sleep(10)
            entered_query = WebDriverHelper(self.driver).getElementValue(locator)
            assert entered_query in self.search_queries, "Search query not entered correctly"
            logging.info("Keys sent to the Search box successfully")
            return True
        except Exception as e:
            logging.error(f"Error while entering search query: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            return False

    @allure.step("Submit search")
    def submit_search(self):
        try:
            locator = (By.XPATH, RazorUI.select_razor)
            WebDriverHelper(self.driver).clickElement(locator)
            logging.info("Search for Razor successfully")
            assert WebDriverHelper(self.driver).isElementClicked(locator), "Search not submitted"
            return True
        except Exception as e:
            logging.error(f"Error while submitting search: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            return False
