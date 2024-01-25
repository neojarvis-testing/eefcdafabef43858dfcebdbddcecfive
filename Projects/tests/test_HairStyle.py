import pytest
from pages.HairStyle import HairStylePage
from base import BaseTest
from utilities.configReader import ConfigReader


class TestGilletteSearch(BaseTest):
    def setUp(self):
        config = ConfigReader()
        url = config.get_url()
        self.driver = self.setUpDriver()
        self.hairstyle = HairStylePage(self.driver)
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.smoke
    def test_hairstyle_search(self):
        self.hairstyle.click_styles()
        self.hairstyle.click_facial()

