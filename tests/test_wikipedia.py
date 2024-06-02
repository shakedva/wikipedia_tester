import pytest
from selenium import webdriver
from scraper.home_page import search
from scraper.search_results_page import find_first_result, check_search_matches


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://he.wikipedia.org/wiki/')
    yield driver
    driver.quit()

# def test_search(driver):
#     text = "clark virgil terry"
#     search(driver, text)
#     li = find_first_result(driver)
#     result = check_search_matches(li)
#     assert result.lower() == text
