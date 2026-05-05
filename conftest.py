# import pytest
# from selene import browser
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# from utils import attach
#
#
# @pytest.fixture(scope='function', autouse=True)
# def setup_browser():
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "128.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#
#     options.capabilities.update(selenoid_capabilities)
#     options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Remote(
#         command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#     browser.config.driver = driver
#
#     yield driver
#
#     attach.add_screenshot(driver)
#     attach.add_page_source(driver)
#     attach.add_console_logs(driver)
#     attach.add_video(driver)
#
#     driver.quit()
import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

load_dotenv()

def get_driver():
    selenoid_url = os.getenv('SELENOID_URL')
    selenoid_enabled = os.getenv('SELENOID_ENABLED', 'false').lower() == 'true'

    if selenoid_enabled and selenoid_url:
        return create_selenoid_driver(selenoid_url)
    else:
        return create_local_chrome_driver()

def create_selenoid_driver(selenoid_url):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options
    )
    return driver

def create_local_chrome_driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")


    driver = webdriver.Chrome(options=options)
    return driver

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    driver = get_driver()
    browser.config.driver = driver

    yield driver

    try:
        attach.add_screenshot(driver)
        attach.add_page_source(driver)
        attach.add_console_logs(driver)
        if os.getenv('SELENOID_ENABLED', 'false').lower() == 'true':
            attach.add_video(driver)
    except Exception as e:
        print(f"Failed to attach artifacts: {e}")

    driver.quit()
