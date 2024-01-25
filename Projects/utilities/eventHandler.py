import os
import logging
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.events import 
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

def configure_logger(log_file_path):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

class EventHandler(AbstractEventListener):
    def __init__(self):
        # log_dir = "/home/coder/project" 
        log_dir = "/Users/tamil/Desktop/PythonSeleniumDemo/Projects" 
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file_path = os.path.join(log_dir, "log.log")
        self.logger = configure_logger(log_file_path)
        self.logged_events = set()

    def _log_event(self, event_text):
        if event_text not in self.logged_events:
            self.logged_events.add(event_text)
            self.logger.info(event_text)

    def before_click(self, element: WebElement, driver: WebDriver):
        element_text = element.text
        element_value = element.get_attribute('value')

        if element_text is None:
            event_text = f"Clicked {element_value}"
        elif element_value is None:
            event_text = f"Clicked {element_text}"
        else:
            event_text = f"Clicked {element_text}{element_value}"

        self._log_event(event_text)

    def before_find(self, by, value, driver):
        if by == By.XPATH:
            if "//" in value or "/html" in value or "//html" in value:
                element = driver.find_element(By.XPATH, value)
                element_name = element.text.strip()
                if not element_name:
                    element_name = element.get_attribute("name") or element.get_attribute("id") or element.get_attribute("class") or "unknown_element"
                value = f"{value}[contains(text(), '{element_name}')]"
                event_text = f"{element_name} #absolute"
            else:
                element = driver.find_element(By.XPATH, value)
                element_name = element.text.strip()
                event_text = element_name

        self._log_event(event_text)

    def before_send_keys(self, element: WebElement, keys_to_send):
        element_info = self._get_xpath_info(element)
        self.logger.info(f"Sending keys to {element_info}: {keys_to_send}")

    def _get_xpath_info(self, element: WebElement):
        xpath = element.get_attribute("xpath")
        element_id = element.get_attribute("id")
        element_name = element.get_attribute("name")
        element_class = element.get_attribute("class")
        if xpath:
            return xpath
        elif element_id:
            return f"element with id='{element_id}'"
        elif element_name:
            return f"element with name='{element_name}'"
        elif element_class:
            return f"element with class='{element_class}'"
        else:
            return "unknown element"
