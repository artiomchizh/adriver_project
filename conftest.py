# import pytest
# from selene.support.shared import browser
#
#
# @pytest.fixture(scope="function", autouse=True)
# def open_browser():
#     browser.config.base_url = 'https://www.adriver.ru/'
#     yield
#     browser.quit()
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    browser.config.driver = webdriver.Chrome(options=chrome_options)
    browser.config.base_url = 'https://www.adriver.ru/'

    yield
    browser.quit()
