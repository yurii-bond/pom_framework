from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

HOME_PAGE_URL = "https://the-internet.herokuapp.com"


# def test_open_website_and_check_title():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(HOME_PAGE_URL)
#     assert driver.title == 'The Internet'
#     sleep(1)
#     driver.quit()
#
#
# def test_open_website_and_check_elements():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(HOME_PAGE_URL)
#     web_element = driver.find_element(By.CLASS_NAME, 'heading')
#     assert web_element.is_displayed()
#     assert web_element.text == 'Welcome to the-internet'
#     sleep(1)
#     driver.quit()
#
#
# def test_open_checkboxes_page_and_check_their_manipulation():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(HOME_PAGE_URL)
#     sleep(2)
#     web_link = driver.find_element(By.LINK_TEXT, 'Checkboxes')
#     assert web_link.is_displayed()
#     web_link.click()
#     sleep(2)
#     assert driver.current_url == f'{HOME_PAGE_URL}/checkboxes'
#     assert driver.find_element(By.TAG_NAME, 'h3').text == 'Checkboxes'
#     checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#     assert len(checkboxes) == 2
#     assert not checkboxes[0].is_selected()
#     assert checkboxes[1].is_selected()
#     sleep(1)
#     checkboxes[0].click()
#     sleep(1)
#     assert checkboxes[0].is_selected()
#     sleep(1)
#     checkboxes[1].click()
#     assert not checkboxes[1].is_selected()
#     sleep(1)
#     driver.back()
#     sleep(1)
#     assert driver.current_url == f'{HOME_PAGE_URL}/'
#     sleep(1)
#     driver.forward()
#     sleep(1)
#     assert driver.current_url == f'{HOME_PAGE_URL}/checkboxes'
#     driver.quit()
#
#
# def test_inputs():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(HOME_PAGE_URL)
#     sleep(1)
#     web_link = driver.find_element(By.LINK_TEXT, 'Inputs')
#     assert web_link.is_displayed()
#     web_link.click()
#     sleep(1)
#     assert driver.current_url == f'{HOME_PAGE_URL}/inputs'
#     assert driver.find_element(By.TAG_NAME, 'h3').text == 'Inputs'
#     sleep(1)
#     input_el = driver.find_element(By.XPATH, "//input[@type='number']")
#     assert input_el.is_displayed()
#     input_el.send_keys(50)
#     sleep(1)
#
#     assert input_el.get_attribute('value') == '50'
#
#     driver.quit()

# ========================================Home task===============================================================


def test_key_press():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(3)
    web_link_presses = driver.find_element(By.LINK_TEXT, 'Key Presses')
    assert web_link_presses.is_displayed()
    web_link_presses.click()
    sleep(2)
    assert driver.current_url == f'{HOME_PAGE_URL}/key_presses'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Key Presses'
    input_element = driver.find_element(By.ID, 'target')
    assert input_element.is_displayed()
    input_element.send_keys(Keys.SPACE)
    sleep(3)

    # verification that the text is iqual to pressed key
    press_result = driver.find_element(By.ID, 'result')
    assert press_result.is_displayed()
    assert press_result.text == 'You entered: SPACE'

    # verifiacation that user can press other button
    input_element.send_keys(Keys.TAB)
    assert press_result.text == 'You entered: TAB'

    # verification that the color text is gree
    GREEN = Color.from_string('green')
    login_button_colour = Color.from_string(press_result.value_of_css_property('color'))
    assert login_button_colour == GREEN
    sleep(2)
    driver.quit()


def test_link_from_page_redirection():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(2)

# verification redirection 'Redirect Link'
    web_link_redirect = driver.find_element(By.LINK_TEXT, 'Redirect Link')
    assert web_link_redirect.is_displayed()
    web_link_redirect.click()
    assert driver.current_url == f'{HOME_PAGE_URL}/redirector'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Redirection'
    sleep(4)

# verification link 'here' is displayed and redirect to the https://the-internet.herokuapp.com/status_codes url
    redirect_link = driver.find_element(By.ID, 'redirect')
    assert redirect_link.is_displayed()
    assert redirect_link.text == 'here'
    redirect_link.click()
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes'
    sleep(2)
    driver.quit()


def test_status_codes_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(2)

    #   verification redirection to the status code page
    status_code_link = driver.find_element(By.LINK_TEXT, 'Status Codes')
    assert status_code_link.is_displayed()
    status_code_link.click()
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'

    # verification link "here" redirection
    redirect_link = driver.find_element(By.LINK_TEXT, 'here')
    assert redirect_link.is_displayed()
    assert redirect_link.text == 'here'
    redirect_link.click()
    assert driver.current_url == "http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml"
    driver.back()

    #   verification list of status codes
    status_codes_list = driver.find_element(By.XPATH, '//ul/li')
    status_codes_list.is_displayed()

    # status code 200
    status_200 = driver.find_element(By.LINK_TEXT, '200')
    assert status_200.is_displayed()
    status_200.click()
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes/200'
    text_200_page = driver.find_element(By.TAG_NAME, 'p')
    assert '200' in text_200_page.text
    link_redirect_to_status_code_page = driver.find_element(By.LINK_TEXT, 'here')
    link_redirect_to_status_code_page.click()

    # status code 301
    status_301 = driver.find_element(By.LINK_TEXT, '301')
    assert status_301.is_displayed()
    status_301.click()
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes/301'
    text_301_page = driver.find_element(By.TAG_NAME, 'p')
    assert '301' in text_301_page.text
    driver.back()

    # status code 404
    status_404 = driver.find_element(By.LINK_TEXT, '404')
    assert status_404.is_displayed()
    status_404.click()
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes/404'
    text_404_page = driver.find_element(By.TAG_NAME, 'p')
    assert '404' in text_404_page.text
    driver.back()

    # status code 500
    status_500 = driver.find_element(By.LINK_TEXT, '500')
    assert status_500.is_displayed()
    status_500.click()
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes/500'
    text_500_page = driver.find_element(By.TAG_NAME, 'p')
    assert '500' in text_500_page.text

    # verification of 'Elemental Selenium redirection'
    elemental_selenium_link = driver.find_element(By.LINK_TEXT, 'Elemental Selenium')
    assert elemental_selenium_link.is_displayed()
    elemental_selenium_link.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://elementalselenium.com/'
    driver.quit()