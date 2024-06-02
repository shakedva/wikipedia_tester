import sys
from selenium import webdriver
from scraper.home_page import HomePage
from scraper.search_results_page import SearchResultsPage
from tests.test_input import validate_input

# TODO handle bad input (number\symbols\etc.)
# TODO no results, you need to notify the user
# TODO If the first results are not the right search, notify the user


def main():
    if len(sys.argv) != 2:
        print("Execution receives one argument: python main.py <arg>")
        sys.exit(1)

    search_input = sys.argv[1]
    if not validate_input(search_input):
        print("Bad input: can only receive alphabetic characters. Special characters and numbers are not allowed.")
        sys.exit(1)

    driver = webdriver.Chrome()

    home_page = HomePage(driver)
    home_page.search(search_input)

    search_results_page = SearchResultsPage(driver)
    li = search_results_page.find_first_result()
    if li is None:
        print("No results found")
        return
    result = search_results_page.check_search_matches(li)

    if result.lower() == search_input.lower():
        print(f"Found {result}")
    else:
        print(
            f"The first result is not what you were looking for! Found {result} instead")


if __name__ == "__main__":
    main()
