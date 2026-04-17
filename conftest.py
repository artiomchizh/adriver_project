# import pytest
# from selene.support.shared import browser
#
#
# @pytest.fixture(scope="function", autouse=True)
# def open_browser():
#     browser.config.base_url = 'https://www.adriver.ru/'
#     yield
# browser.quit()
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield driver
