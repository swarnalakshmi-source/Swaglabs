from pages.base_page import BasePage
from pages.components.header import Header


def slugify(product_name: str) -> str:
    """'Sauce Labs Backpack' -> 'sauce-labs-backpack' (used in data-test ids)."""
    return product_name.lower().replace(' ', '-')


class InventoryPage(BasePage):
    path = '/inventory.html'

    SORT_NAME_AZ = 'az'
    SORT_NAME_ZA = 'za'
    SORT_PRICE_LOW_HIGH = 'lohi'
    SORT_PRICE_HIGH_LOW = 'hilo'

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)
        self.title = page.get_by_test_id('title')
        self.items = page.get_by_test_id('inventory-item')
        self.item_names = page.get_by_test_id('inventory-item-name')
        self.item_prices = page.get_by_test_id('inventory-item-price')
        self.sort_dropdown = page.get_by_test_id('product-sort-container')

    def product_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def product_prices(self) -> list[float]:
        return [float(text.replace('$', '')) for text in self.item_prices.all_inner_texts()]

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)
        return self

    def add_to_cart(self, product_name: str):
        self.page.get_by_test_id(f'add-to-cart-{slugify(product_name)}').click()
        return self

    def remove_from_cart(self, product_name: str):
        self.page.get_by_test_id(f'remove-{slugify(product_name)}').click()
        return self

    def open_cart(self):
        return self.header.open_cart()
