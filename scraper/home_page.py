from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def search(driver, text):
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@class='cdx-text-input__input']"))
    )

    search_input.send_keys(text)
    search_button = driver.find_element(
        by=By.CLASS_NAME, value='cdx-search-input__end-button')

    search_button.click()
