from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PageBase:

    types = {
        'name': By.NAME,
        'id': By.ID,
        'xpath': By.XPATH
    }

    def __init__(self, wait):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.wd = webdriver.Chrome(options=self.options)
        self.wd.maximize_window()
        self.wait = wait

    def navigate_to_page(self, page_url):
        self.wd.get(page_url)

    def click_element(self, locator_type, locator_value):
        wait = WebDriverWait(self.wd, 10)
        wait.until(EC.element_to_be_clickable((self.types[locator_type], locator_value)))
        self.wd.find_element(self.types[locator_type], locator_value).click()

    def wait_for_text_to_be_present(self, locator_type, locator_value, desired_text):
        wait = WebDriverWait(self.wd, 10)
        wait.until(EC.text_to_be_present_in_element((self.types[locator_type], locator_value), desired_text))
