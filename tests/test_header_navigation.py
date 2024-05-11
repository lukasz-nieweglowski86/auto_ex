from selenium import webdriver
import repo.auto_ex.pages.home_page as homepage_locators
import repo.auto_ex.pages.casino_page as casino_locators
import repo.auto_ex.pages.header as header
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
wd = webdriver.Chrome(options=options)
wd.maximize_window()

types = {
    'name': By.NAME,
    'id': By.ID,
    'xpath': By.XPATH
}


def navigate_to_page(page_url):
    wd.get(page_url)


def click_element(locator_type, locator_value):
    wd.find_element(locator_type, locator_value).click()


def wait_for_text_to_be_present(locator_type, locator_value, desired_text):
    wait = WebDriverWait(wd, 10)
    wait.until(EC.text_to_be_present_in_element((types[locator_type], locator_value), desired_text))


def test_switch_between_homepage_to_casino_page():
    navigate_to_page(homepage_locators.page_url)  # Precondition 1
    click_element('xpath', header.buttons['casino_tab'])  # Step 1
    wait_for_text_to_be_present(types['xpath'], '//h1[text()="New games"]', 'New games')
    assert wd.current_url == casino_locators.page_url  # Assertion 1
    assert wd.find_element(types['xpath'], '//h1[text()="New games"]').is_displayed()  # Assertion 2


def test_switch_between_casino_page_to_homepage():
    navigate_to_page(casino_locators.page_url)  # Precondition 1
    click_element('xpath', header.buttons['home_tab'])  # Step 1
    wait_for_text_to_be_present(types['xpath'], '//main[text()="Something..."]', 'Something...')
    assert wd.current_url == homepage_locators.page_url  # Assertion 1
    assert wd.find_element(types['xpath'], '//main[text()="Something..."]').is_displayed()  # Assertion 2
    wd.quit()
