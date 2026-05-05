import allure
from selene import be
from selene.support.shared import browser


class AgencyPage:
    def __init__(self):
        self.page_title = browser.element('.agency-top-title')


    @allure.step("Wait for agency page to load")
    def should_be_loaded(self):
        self.page_title.should(be.visible)
        return self


