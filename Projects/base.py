import unittest
import pytest
import os
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.eventHandler import EventHandler  
from utilities.logger import configure_logger

configure_logger()

class BaseTest(unittest.TestCase):
    def setUpDriver(self):
        event_handler = EventHandler()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        remote_url = "https://4444-seleniuminstance3.premiumproject.examly.io"
        driver = webdriver.Remote(command_executor=remote_url, options=options)
        
        event_driver = EventFiringWebDriver(driver, event_handler)
        return event_driver

if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    tests_directory = os.path.join(current_directory, 'tests')
    pytest.main(['-v', tests_directory, '--alluredir', 'Report'])
