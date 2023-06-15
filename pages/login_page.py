from playwright.sync_api import sync_playwright


class LoginPage:
    def __init__(self, page):
        self.page = page

    def _enter_username(self, username):
        self.page.fill('input[name="username"]', username)

    def _enter_password(self, password):
        self.page.fill('input[name="password"]', password)

    def _click_login_button(self):
        self.page.click('button[type="submit"]')

    def login(self, username, password):
        self._enter_username(username)
        self._enter_password(password)
        self._click_login_button()