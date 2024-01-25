import pytest
from pages.razor import GillettePage
from base import BaseTest
from utilities.configReader import ConfigReader

class TestGilletteSearch(BaseTest):
    def setUp(self):
        config = ConfigReader()
        url = config.get_url()
        self.driver = self.setUpDriver()
        self.gillette_page = GillettePage(self.driver)
        self.driver.get(url)
 
    def tearDown(self):
        self.driver.quit()

    @pytest.mark.smoke
    def test_gillette_search(self):        
        self.gillette_page.click_search_box()
        self.gillette_page.enter_search_query()
        self.gillette_page.submit_search()


