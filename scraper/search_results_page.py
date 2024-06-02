from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def find_first_result(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//li//div[@class='searchresult']")
                )
            )
        except TimeoutException:
            return None

    @classmethod
    def check_search_matches(cls, li):
        if li is None:
            return ''
        search_matches = li.find_elements(
            by=By.XPATH,
            value=".//span[@class='searchmatch']"
        )
        return ' '.join(span.text for span in search_matches)
