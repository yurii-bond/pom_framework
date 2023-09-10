from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

HOME_PAGE_URL = "https://the-internet.herokuapp.com"

def test_open_website_and_check_title():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    assert driver.title == 'The Internet'
    sleep(1)
    driver.quit()


def test_open_website_and_check_elements():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    web_element = driver.find_element(By.CLASS_NAME, 'heading')
    assert web_element.is_displayed()
    assert web_element.text == 'Welcome to the-internet'
    sleep(1)
    driver.quit()


def test_open_checkboxes_page_and_check_their_manipulation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(2)
    web_link = driver.find_element(By.LINK_TEXT, 'Checkboxes')
    assert web_link.is_displayed()
    web_link.click()
    sleep(2)
    assert driver.current_url == f'{HOME_PAGE_URL}/checkboxes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Checkboxes'
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    assert len(checkboxes) == 2
    assert not checkboxes[0].is_selected()
    assert checkboxes[1].is_selected()
    sleep(1)
    checkboxes[0].click()
    sleep(1)
    assert checkboxes[0].is_selected()
    sleep(1)
    checkboxes[1].click()
    assert not checkboxes[1].is_selected()
    sleep(1)
    driver.back()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/'
    sleep(1)
    driver.forward()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/checkboxes'
    driver.quit()


def test_inputs():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(1)
    web_link = driver.find_element(By.LINK_TEXT, 'Inputs')
    assert web_link.is_displayed()
    web_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/inputs'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Inputs'
    sleep(1)
    input_el = driver.find_element(By.XPATH, "//input[@type='number']")
    assert input_el.is_displayed()
    input_el.send_keys(50)
    sleep(1)

    assert input_el.get_attribute('value') == '50'

    driver.quit()

def test_key_presses():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(f'{HOME_PAGE_URL}/key_presses')
    sleep(1)
    input_el = driver.find_element(By.XPATH, "//input[@type='text']")
    input_el.send_keys('1 ')
    sleep(1)
    result = driver.find_element(By.ID, 'result')
    assert result.text == 'You entered: SPACE'
    sleep(1)
    driver.quit()

def test_redirector():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(f'{HOME_PAGE_URL}/redirector')
    sleep(1)
    redirector = driver.find_element(By.ID, "redirect")
    redirector.click()
    sleep(1)
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    driver.quit()

def test_status_codes():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(f'{HOME_PAGE_URL}/status_codes')
    sleep(1)
    status_codes = driver.find_element(By.LINK_TEXT, "200")
    status_codes.click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//*[contains(text(), "returned a 200")]')
    here = driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
    here.click()
    sleep(1)
    status_codes = driver.find_element(By.LINK_TEXT, "301")
    status_codes.click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//*[contains(text(), "returned a 301")]')
    here1 = driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
    here1.click()
    sleep(1)
    status_codes = driver.find_element(By.LINK_TEXT, "404")
    status_codes.click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//*[contains(text(), "returned a 404")]')
    here2 = driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
    here2.click()
    sleep(1)
    status_codes = driver.find_element(By.LINK_TEXT, "500")
    status_codes.click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//*[contains(text(), "returned a 500")]')
    here2 = driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
    here2.click()
    sleep(1)
    driver.quit()
