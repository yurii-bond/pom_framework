from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import pytest

class TestKeyPresses:

    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        yield
        self.driver.quit()

    def test_key_press_a(self, setup):
        self.driver.get("https://the-internet.herokuapp.com/key_presses")
        input_field = self.driver.find_element_by_id("target")
        input_field.send_keys(Keys.A)
        result = self.driver.find_element_by_id("result").text
        assert result == "You entered: A"