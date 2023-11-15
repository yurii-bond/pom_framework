import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver_setup(request):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    yield driver
    driver.quit()

def test_key_presses(driver_setup):
    driver = driver_setup
    driver.get("https://the-internet.herokuapp.com/key_presses")
    input_field = driver.find_element_by_id("target")
    input_field.send_keys(Keys.A)
    result = driver.find_element_by_id("result").text
    assert result == "You entered: A"

def test_redirector(driver_setup):
    driver = driver_setup
    driver.get("https://the-internet.herokuapp.com/redirector")
    redirect_link = driver.find_element_by_link_text("here")
    redirect_link.click()
    assert "status_codes" in driver.current_url

def test_status_codes(driver_setup):
    driver = driver_setup
    driver.get("https://the-internet.herokuapp.com/status_codes/200")
    assert "200" in driver.page_source