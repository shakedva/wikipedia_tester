from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


def find_first_result(driver):
    try:
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li//div[@class='searchresult']"))
        )
    except TimeoutException:  # TODO
        return None


def check_search_matches(li):
    if li is None:
        return ''
    search_matches = li.find_elements(
        by=By.XPATH, value=".//span[@class='searchmatch']")
    return ' '.join(span.text for span in search_matches)
