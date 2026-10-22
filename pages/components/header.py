from playwright.sync_api import Page


class Header:
    """Top bar and side menu shown on every page after login."""

    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.get_by_test_id('shopping-cart-link')
        self.cart_badge = page.get_by_test_id('shopping-cart-badge')
        self.menu_button = page.get_by_role('button', name='Open Menu')
        self.logout_link = page.get_by_test_id('logout-sidebar-link')

    def cart_count(self) -> int:
        """Number on the cart badge; 0 when the badge is not displayed."""
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def open_cart(self):
        from pages.cart_page import CartPage
        self.cart_link.click()
        return CartPage(self.page).expect_loaded()

    def logout(self):
        from pages.login_page import LoginPage
        self.menu_button.click()
        self.logout_link.click()
        return LoginPage(self.page).expect_loaded()
