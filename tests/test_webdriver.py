
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

HOME_PAGE_URL = "https://the-internet.herokuapp.com"


def test_open_website_and_check_title():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)

    WebDriverWait(driver, 10).until(EC.title_is('The Internet'))

    assert driver.title == 'The Internet'
    driver.quit()


def test_open_website_and_check_elements():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)

    try:
        WebDriverWait(driver, 30, poll_frequency=100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "heading"))
        )
    except:
        driver.quit()

    web_element = driver.find_element(By.CLASS_NAME, 'heading')
    assert web_element.is_displayed()
    assert web_element.text == 'Welcome to the-internet'
    driver.quit()


def test_open_checkboxes_page_and_check_their_manipulation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)

    web_link = driver.find_element(By.LINK_TEXT, 'Checkboxes')
    assert web_link.is_displayed()
    web_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains('/checkboxes'))
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), 'Checkboxes'))

    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    assert len(checkboxes) == 2
    assert not checkboxes[0].is_selected()
    assert checkboxes[1].is_selected()

    checkboxes[0].click()
    assert checkboxes[0].is_selected()
    checkboxes[1].click()
    assert not checkboxes[1].is_selected()

    driver.back()
    driver.forward()

    driver.quit()


def test_inputs():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)

    web_link = driver.find_element(By.LINK_TEXT, 'Inputs')
    assert web_link.is_displayed()
    web_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains('/inputs'))
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), 'Inputs'))

    input_el = driver.find_element(By.XPATH, "//input[@type='number']")
    assert input_el.is_displayed()
    input_el.send_keys(50)
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.XPATH, "//input[@type='number']"), '50'))

    driver.quit()


def test_hovers():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)

    web_link = driver.find_element(By.LINK_TEXT, 'Hovers')
    assert web_link.is_displayed()
    web_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains('/hovers'))
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), 'Hovers'))

    avatars = driver.find_elements(By.XPATH, "//div[@class='figure']")
    for avatar in avatars:

        WebDriverWait(driver, 10).until_not(EC.visibility_of(avatar.find_element(By.XPATH, ".//div/h5")))

    driver.quit()


def changes_test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)

    web_link = driver.find_element(By.LINK_TEXT, 'Drag and Drop')
    assert web_link.is_displayed()
    web_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains('/drag_and_drop'))
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), 'Drag and Drop'))

    column_a = driver.find_element(By.ID, "column-a")
    column_b = driver.find_element(By.ID, "column-b")

    assert column_a.text == "A"
    assert column_b.text == "B"

    action = webdriver.ActionChains(driver)
    action.drag_and_drop(column_b, column_a).perform()

    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'column-a'), 'B'))

    driver.quit()


def test_context_menu():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)

    web_link = driver.find_element(By.LINK_TEXT, 'Context Menu')
    assert web_link.is_displayed()
    web_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains('/context_menu'))
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), 'Context Menu'))

    hot_spot = driver.find_element(By.ID, "hot-spot")

    action = webdriver.ActionChains(driver)
    action.context_click(hot_spot).perform()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "You selected a context menu"
    alert.accept()

    driver.quit()


def test_file_upload():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)

    web_link = driver.find_element(By.LINK_TEXT, 'File Upload')
    assert web_link.is_displayed()
    web_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains('/upload'))
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), 'File Uploader'))

    file_path = os.getcwd().replace("/tests", "/src/resources/image.png")
    driver.find_element(By.ID, "file-upload").send_keys(file_path)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'file-submit'))).click()

    driver.quit()



if __name__ == "__main__":
    # Вызов функций для выполнения тестов
    test_open_website_and_check_title()
    test_open_website_and_check_elements()
    test_open_checkboxes_page_and_check_their_manipulation()
    test_inputs()
    test_hovers()
    changes_test_drag_and_drop()
    test_context_menu()
    test_file_upload()
