from selenium import webdriver
from contextlib import contextmanager


@contextmanager
def selenium_driver():
    driver = webdriver.Chrome()
    try:
        yield driver
    finally:
        driver.quit()
