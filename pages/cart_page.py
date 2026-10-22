from pages.base_page import BasePage
from pages.components.header import Header
from pages.inventory_page import slugify


class CartPage(BasePage):
    path = '/cart.html'

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)
        self.item_names = page.get_by_test_id('inventory-item-name')
        self.checkout_button = page.get_by_test_id('checkout')
        self.continue_shopping_button = page.get_by_test_id('continue-shopping')

    def product_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def remove(self, product_name: str):
        self.page.get_by_test_id(f'remove-{slugify(product_name)}').click()
        return self

    def checkout(self):
        from pages.checkout_page import CheckoutInfoPage
        self.checkout_button.click()
        return CheckoutInfoPage(self.page).expect_loaded()

    def continue_shopping(self):
        from pages.inventory_page import InventoryPage
        self.continue_shopping_button.click()
        return InventoryPage(self.page).expect_loaded()
