import argparse
import re
from scraper import HomePage, SearchResultsPage, selenium_driver


def validate_input(input):
    return re.match("^[A-Za-z ]+$", input)


def search(query):
    with selenium_driver() as driver:
        home_page = HomePage(driver)
        home_page.search(query)
        search_results_page = SearchResultsPage(driver)
        li = search_results_page.find_first_result()
        if li is None:
            print('No results found')
            return
        result = search_results_page.check_search_matches(li)

        if result.lower() == query.lower():
            print(f'Found {result}')
        else:
            print(
                f'''
                The first result is not what you were looking for! Found {result} instead
                '''
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-q',
        '--query',
        type=str,
        help='Text to search in Wikipedia',
        required=True
    )
    args = parser.parse_args()
    query = args.query.strip()
    if not validate_input(query):
        print('Bad input: can only receive alphabetic characters. Special characters and numbers are not allowed.')
        return
    search(query)


if __name__ == '__main__':
    main()
