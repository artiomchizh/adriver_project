import allure
from selene.support import by
from selene.support.conditions import have, be
from selene.support.shared import browser

from pages.ad_river import AdRiver

class TestAdRiver:
    with allure.step("main page opens"):
        def test_01(self):

            adriver = AdRiver()
            adriver.open()
            assert adriver.page_title_contains('AdRiver')
    with allure.step("login button works"):
        def test_02(self):
            adriver = AdRiver()
            adriver.open()
            adriver.click_login_button()
            assert adriver.is_login_form_displayed()
    with allure.step("search functionality"):
        def test_03(self):
            adriver = AdRiver()
            adriver.open()
            adriver.search_for('реклама')
            count = adriver.get_search_results_count()
            assert count > 0
    with allure.step("agency navigation"):
        def test_04(self):
            adriver = AdRiver()
            adriver.open()
            adriver.navigate_to_agency()
            assert 'agency' in browser.driver.current_url
    with allure.step("header links present"):
        def test_05(self):
            adriver = AdRiver()
            adriver.open()
            assert adriver.check_header_links()
    with allure.step("footer links navigation"):
        def test_06(self):
            adriver = AdRiver()
            adriver.open()
            adriver.scroll_to_bottom()
            result = adriver.click_and_check_footer_link('Политика конфиденциальности')
            assert result
    with allure.step("responsive elements visible"):
        def test_07(self):

            adriver = AdRiver()
            adriver.open()
            adriver.header_login_button.should(be.visible)
            adriver.agency_link.should(be.visible)
            adriver.search_input.should(be.visible)
    with allure.step("page elements interactable"):
        def test_08(self):
            adriver = AdRiver()
            adriver.open()

            current_url = browser.driver.current_url
            adriver.company_link.should(be.clickable).click()
            assert browser.driver.current_url != current_url

            adriver.open()

            current_url = browser.driver.current_url
            adriver.news_link.should(be.clickable).click()
            assert browser.driver.current_url != current_url



