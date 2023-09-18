from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

from selenium.webdriver.support.wait import WebDriverWait


HOME_PAGE_URL = "https://the-internet.herokuapp.com"


def test_open_website_and_check_title():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.set_script_timeout(10)
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    assert driver.title == 'The Internet'
    sleep(1)
    driver.quit()


def test_open_website_and_check_elements():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    try:
        element = WebDriverWait(driver, 30, poll_frequency=100).until(EC.presence_of_element_located((By.ID, "id-of-element")))
    except:
        driver.quit()
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


def test_hovers():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(1)
    web_link = driver.find_element(By.LINK_TEXT, 'Hovers')
    assert web_link.is_displayed()
    web_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/hovers'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Hovers'
    sleep(1)

    avatars = driver.find_elements(By.XPATH, "//div[@class='figure']")
    for i, avatar in enumerate(avatars):
        invisible_el = driver.find_element(By.XPATH, f"//div[@class='figure'][{i+1}]/div/h5")

    driver.quit()


def changes_test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(1)
    web_link = driver.find_element(By.LINK_TEXT, 'Drag and Drop')
    assert web_link.is_displayed()
    web_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/drag_and_drop'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Drag and Drop'
    sleep(1)

    column_a = driver.find_element(By.ID, "column-a")
    column_b = driver.find_element(By.ID, "column-b")
    assert column_a.text == "A"
    assert column_b.text == "B"
    sleep(1)

    action = ActionChains(driver)
    action.drag_and_drop(column_b, column_a).perform()
    sleep(1)

    column_a = driver.find_element(By.ID, "column-a")
    column_b = driver.find_element(By.ID, "column-b")

    assert column_a.text == "B"

    driver.quit()


def test_context_menu():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(1)
    web_link = driver.find_element(By.LINK_TEXT, 'Context Menu')
    assert web_link.is_displayed()
    web_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/context_menu'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Context Menu'
    sleep(1)
    hot_spot = driver.find_element(By.ID, "hot-spot")
    actions = ActionChains(driver)
    actions.context_click(hot_spot).perform()
    sleep(2)

    alert = Alert(driver)
    assert alert.text == "You selected a context menu"
    alert.accept()

    sleep(2)

    driver.quit()


def test_file_upload():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(1)
    web_link = driver.find_element(By.LINK_TEXT, 'File Upload')
    assert web_link.is_displayed()
    web_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/upload'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'File Uploader'
    sleep(2)
    file_path = os.getcwd().replace("/tests", "/src/resources/image.png")
    driver.find_element(By.ID, "file-upload").send_keys(file_path)
    sleep(3)
    driver.find_element(By.ID, 'file-submit')


