import allure
from selene import have, be, by
from selene.support.shared import browser


class AdRiver:
    def __init__(self):
        self.header_login_button = browser.element('a[href*="members"]')
        self.search_input = browser.element('[name="s"]')
        self.agency_link = browser.element(by.text('Агентствам'))
        self.company_link = browser.element(by.text('О компании'))
        self.news_link = browser.element(by.text('Новости'))
        self.contacts_link = browser.element(by.text('Контакты'))
        self.privacy_policy_link = browser.element(by.text('Политика конфиденциальности'))
        self.search_results = browser.all('.search-block-elenent')
        self.login_form = browser.element('.entrance-form-block')

    @allure.step("Open main page")
    def open(self):
        browser.open('https://www.adriver.ru/')

    @allure.step("Click login button")
    def click_login_button(self):
        self.header_login_button.should(be.clickable).click()

    @allure.step("Is login form displayed")
    def is_login_form_displayed(self):
        return self.login_form.with_(timeout=10).should(be.visible)

    @allure.step("Search for")
    def search_for(self, query):
        self.search_input.should(be.enabled).type(query).press_enter()

    @allure.step("Get search results count")
    def get_search_results_count(self):
        self.search_results.with_(timeout=10).should(have.size_greater_than_or_equal(0))
        return len(self.search_results)

    @allure.step("Navigate to agency")
    def navigate_to_agency(self):
        self.agency_link.should(be.clickable).click()

    @allure.step("Check header links")
    def check_header_links(self):
        self.company_link.should(be.visible)
        self.news_link.should(be.visible)
        self.contacts_link.should(be.visible)
        return True

    @allure.step("Click footer link")
    def click_and_check_footer_link(self, link_text):
        footer_link = browser.element(by.text(link_text))
        current_url = browser.driver.current_url
        footer_link.should(be.clickable).click()
        return browser.driver.current_url != current_url

    @allure.step("Scroll to bottom")
    def scroll_to_bottom(self):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    def page_title_contains(self, text):
        return text in browser.driver.title
