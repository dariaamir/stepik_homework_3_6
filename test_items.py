from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
submit_button_selector = (By.CSS_SELECTOR, '#add_to_basket_form button[type="submit"]')


def test_add_to_basket_button(browser):
    browser.get(url)
    WebDriverWait(browser, 5).until(ec.visibility_of_element_located(submit_button_selector))
    assert browser.find_element(*submit_button_selector), 'Error: Submit button is not displayed'
