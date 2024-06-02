from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.navigate()

    def navigate(self):
        self.driver.get('https://he.wikipedia.org/wiki/')

    def search(self, text):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@class='cdx-text-input__input']"))
        )

        search_input.send_keys(text)
        search_button = self.driver.find_element(
            by=By.CLASS_NAME, value='cdx-search-input__end-button')

        search_button.click()
