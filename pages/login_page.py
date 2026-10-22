from playwright.sync_api import expect

from data.users import User
from pages.base_page import BasePage


class LoginPage(BasePage):
    path = '/'

    def __init__(self, page):
        super().__init__(page)
        self.username = page.get_by_test_id('username')
        self.password = page.get_by_test_id('password')
        self.login_button = page.get_by_test_id('login-button')
        self.error = page.get_by_test_id('error')

    def expect_loaded(self):
        expect(self.login_button).to_be_visible()
        return self

    def login(self, username: str, password: str):
        """Submit the form and stay on this object; use for negative tests."""
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        return self

    def login_as(self, user: User):
        """Successful login; returns the inventory page."""
        from pages.inventory_page import InventoryPage
        self.login(user.username, user.password)
        return InventoryPage(self.page).expect_loaded()
