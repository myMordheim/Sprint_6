import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.close()