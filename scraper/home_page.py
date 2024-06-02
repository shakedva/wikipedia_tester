from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from search_results import find_first_result, check_search_matches


def search(driver, text):
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@class='cdx-text-input__input']"))
    )

    search_input.send_keys(text)
    search_button = driver.find_element(
        by=By.CLASS_NAME, value='cdx-search-input__end-button')

    search_button.click()


driver = webdriver.Chrome()
driver.get('https://he.wikipedia.org/wiki/')
text = "clark virgil terry"
search(driver, text)
li = find_first_result(driver)
result = check_search_matches(li)
print(f"{result.lower() == text}")
driver.quit()
