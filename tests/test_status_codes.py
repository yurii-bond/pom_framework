from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import pytest

class TestStatusCodes:

    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        yield
        self.driver.quit()

    def test_status_code_200(self, setup):
        self.driver.get("https://the-internet.herokuapp.com/status_codes/200")
        assert "200" in self.driver.page_source