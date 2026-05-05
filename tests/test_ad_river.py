
import allure
from selene.support import by
from selene.support.conditions import have, be
from selene.support.shared import browser

from pages.main_page import MainPage
from pages.agency_page import AgencyPage
from pages.login_page import LoginPage


@allure.feature("AdRiver Website")
@allure.story("Main Page Functionality")
def setup_module():
    browser.config.base_url = 'https://www.adriver.ru/'


def teardown_module():
    browser.quit()

@allure.title("Main page opens successfully")
@allure.description("Verify that main page loads and has correct title")
def test_main_page_opens():
    main_page = MainPage().open()
    assert main_page.page_title_contains('AdRiver')

@allure.title("Login button works")
@allure.description("Click login button and verify login form appears")
def test_login_button_works():
    main_page = MainPage().open()
    login_page = main_page.click_login_button()
    login_page.should_be_loaded()

@allure.title("Search functionality works")
@allure.description("Search for 'реклама' and verify results appear")
def test_search_functionality():
    main_page = MainPage().open()
    search_results_page = main_page.search_for('реклама')
    count = search_results_page.get_results_count()
    assert count > 0


@allure.title("Navigation to Agency page")
@allure.description("Navigate to Agency page and verify it loads")
def test_agency_navigation():
    main_page = MainPage().open()
    agency_page = main_page.navigate_to_agency()
    agency_page.should_be_loaded()


