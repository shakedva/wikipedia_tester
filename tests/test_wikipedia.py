import pytest
from scraper import HomePage, SearchResultsPage, selenium_driver


@pytest.fixture
def driver():
    with selenium_driver() as driver:
        yield driver

# def test_search(driver):
#     text = "clark virgil terry"
#     search(driver, text)
#     li = find_first_result(driver)
#     result = check_search_matches(li)
#     assert result.lower() == text
