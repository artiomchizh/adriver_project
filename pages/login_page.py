import allure
from selene import be
from selene.support.shared import browser


class LoginPage:
    def __init__(self):
        self.username_field = browser.element('[name="login"]')
        self.password_field = browser.element('[name="Passwd"]')
        self.submit_button = browser.element('[type="submit"]')

    @allure.step("Wait for login page to load")
    def should_be_loaded(self):
        self.username_field.should(be.visible)
        return self

    @allure.step("Login with credentials")
    def login(self, username, password):
        self.username_field.should(be.enabled).type(username)
        self.password_field.should(be.enabled).type(password)
        self.submit_button.click()
        return self
