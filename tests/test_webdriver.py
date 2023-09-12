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


def test_key_presses_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(1)
    web_link = driver.find_element(By.LINK_TEXT, 'Key Presses')
    assert web_link.is_displayed()
    web_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/key_presses'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Key Presses'
    sleep(1)
    input_el = driver.find_element(By.XPATH, "//*[@id='target']")
    assert input_el.is_displayed()
    # SPACE button
    input_el.send_keys(Keys.BACK_SPACE)
    assert driver.find_element(By.ID, 'result').text == 'You entered: BACK_SPACE'
    sleep(1)
    # TAB button
    input_el.send_keys(Keys.TAB)
    assert driver.find_element(By.ID, 'result').text == 'You entered: TAB'
    sleep(1)
    # ESCAPE button
    input_el.send_keys(Keys.ESCAPE)
    assert driver.find_element(By.ID, 'result').text == 'You entered: ESCAPE'
    sleep(1)
    # ENTER when the INPUT FIELD is not in FOCUS
    driver.find_element(By.XPATH, "//body").send_keys(Keys.ENTER)
    assert driver.find_element(By.ID, 'result').text == 'You entered: ENTER'
    sleep(1)
    # ENTER when the INPUT FIELD is in FOCUS
    input_el.send_keys(Keys.ENTER)
    assert driver.find_element(By.ID, 'result').text == ''
    driver.quit()


def test_redirection_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(1)
    web_link = driver.find_element(By.LINK_TEXT, 'Redirect Link')
    assert web_link.is_displayed()
    web_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/redirector'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Redirection'
    sleep(1)
    redirect_link = driver.find_element(By.XPATH, "//*[@id='redirect']")
    assert redirect_link.is_displayed()
    redirect_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    driver.quit()


def test_status_codes_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(1)
    web_link = driver.find_element(By.LINK_TEXT, 'Status Codes')
    assert web_link.is_displayed()
    web_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    sleep(1)

    # Status 200

    redirect_link_200 = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/a")
    assert redirect_link_200.is_displayed()
    redirect_link_200.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes/200'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    text_200 = driver.find_element(By.XPATH, "//*[@id='content']/div/p")
    assert text_200.is_displayed()
    assert driver.find_element(By.XPATH,
                               "//*[@id='content']/div/p").text == 'This page returned a 200 status code.\n''\n''For a definition and common list of HTTP status codes, go here'
    back_redirect_link = driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
    assert back_redirect_link.is_displayed()
    back_redirect_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    sleep(1)

    # Status 301

    redirect_link_301 = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/a")
    assert redirect_link_301.is_displayed()
    redirect_link_301.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes/301'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    text_200 = driver.find_element(By.XPATH, "//*[@id='content']/div/p")
    assert text_200.is_displayed()
    assert driver.find_element(By.XPATH,"//*[@id='content']/div/p").text == 'This page returned a 301 status code.\n''\n''For a definition and common list of HTTP status codes, go here'
    back_redirect_link = driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
    assert back_redirect_link.is_displayed()
    back_redirect_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    sleep(1)

    # Status 404

    redirect_link_404 = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/a")
    assert redirect_link_404.is_displayed()
    redirect_link_404.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes/404'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    text_200 = driver.find_element(By.XPATH, "//*[@id='content']/div/p")
    assert text_200.is_displayed()
    assert driver.find_element(By.XPATH, "//*[@id='content']/div/p").text == 'This page returned a 404 status code.\n''\n''For a definition and common list of HTTP status codes, go here'
    back_redirect_link = driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
    assert back_redirect_link.is_displayed()
    back_redirect_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    sleep(1)

    # Status 500

    redirect_link_500 = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[4]/a")
    assert redirect_link_500.is_displayed()
    redirect_link_500.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes/500'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    text_200 = driver.find_element(By.XPATH, "//*[@id='content']/div/p")
    assert text_200.is_displayed()
    assert driver.find_element(By.XPATH, "//*[@id='content']/div/p").text == 'This page returned a 500 status code.\n''\n''For a definition and common list of HTTP status codes, go here'
    back_redirect_link = driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
    assert back_redirect_link.is_displayed()
    back_redirect_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    sleep(1)

    # Link redirection "here"

    redirect_link = driver.find_element(By.LINK_TEXT, 'here')
    assert redirect_link.is_displayed()
    assert redirect_link.text == 'here'
    redirect_link.click()
    assert driver.current_url == "http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml"
    sleep(2)
    driver.quit()
