from selene.support import by
from selene.support.conditions import have, be
from selene.support.shared import browser

from pages.ad_river import AdRiver

class TestAdRiver:

    def test_01_main_page_opens(self):

        adriver = AdRiver()
        adriver.open()
        assert adriver.page_title_contains('AdRiver')

    def test_02_login_button_works(self):
        adriver = AdRiver()
        adriver.open()
        adriver.click_login_button()
        assert adriver.is_login_form_displayed(), "Форма авторизации не отображается"

    def test_03_search_functionality(self):
        adriver = AdRiver()
        adriver.open()
        adriver.search_for('реклама')
        count = adriver.get_search_results_count()
        assert count > 0

    def test_04_agency_navigation(self):
        adriver = AdRiver()
        adriver.open()
        adriver.navigate_to_agency()
        assert 'agency' in browser.driver.current_url

    def test_05_header_links_present(self):
        adriver = AdRiver()
        adriver.open()
        assert adriver.check_header_links()

    def test_06_footer_links_navigation(self):
        adriver = AdRiver()
        adriver.open()
        adriver.scroll_to_bottom()
        result = adriver.click_and_check_footer_link('Политика конфиденциальности')
        assert result

    def test_07_responsive_elements_visible(self):

        adriver = AdRiver()
        adriver.open()
        # Проверяем видимость основных элементов
        adriver.header_login_button.should(be.visible)
        adriver.agency_link.should(be.visible)
        adriver.search_input.should(be.visible)

    def test_8_page_elements_interactable(self):
        adriver = AdRiver()
        adriver.open()

        current_url = browser.driver.current_url
        adriver.company_link.should(be.clickable).click()
        assert browser.driver.current_url != current_url

        adriver.open()

        current_url = browser.driver.current_url
        adriver.news_link.should(be.clickable).click()
        assert browser.driver.current_url != current_url



