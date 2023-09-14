from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import pytest

class TestRedirector:

    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        yield
        self.driver.quit()

    def test_redirect(self, setup):
        self.driver.get("https://the-internet.herokuapp.com/redirector")
        redirect_link = self.driver.find_element_by_link_text("here")
        redirect_link.click()
        assert "status_codes" in self.driver.current_url