from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.abtest_xpath = "//a[@href='/abtest']"
        self.add_remove_elements_xpath = "//a[@href='/add_remove_elements']"
        self.basic_auth_xpath = "//a[@href='/basic_auth']"

    def click_on_link(self, web_elements_xpath):
        self.driver.find_element(By.XPATH, web_elements_xpath).click()
