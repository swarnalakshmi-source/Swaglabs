"""The three checkout screens, one class each."""
from pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    path = '/checkout-step-one.html'

    def __init__(self, page):
        super().__init__(page)
        self.first_name = page.get_by_test_id('firstName')
        self.last_name = page.get_by_test_id('lastName')
        self.postal_code = page.get_by_test_id('postalCode')
        self.continue_button = page.get_by_test_id('continue')
        self.cancel_button = page.get_by_test_id('cancel')
        self.error = page.get_by_test_id('error')

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        return self

    def continue_to_overview(self):
        """Valid data: moves on to the overview page."""
        self.continue_button.click()
        return CheckoutOverviewPage(self.page).expect_loaded()

    def submit(self):
        """Stay on this page (used for validation-error tests)."""
        self.continue_button.click()
        return self


class CheckoutOverviewPage(BasePage):
    path = '/checkout-step-two.html'

    def __init__(self, page):
        super().__init__(page)
        self.item_names = page.get_by_test_id('inventory-item-name')
        self.subtotal_label = page.get_by_test_id('subtotal-label')
        self.tax_label = page.get_by_test_id('tax-label')
        self.total_label = page.get_by_test_id('total-label')
        self.finish_button = page.get_by_test_id('finish')

    @staticmethod
    def _amount(label_text: str) -> float:
        return float(label_text.split('$')[-1])

    def product_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def subtotal(self) -> float:
        return self._amount(self.subtotal_label.inner_text())

    def tax(self) -> float:
        return self._amount(self.tax_label.inner_text())

    def total(self) -> float:
        return self._amount(self.total_label.inner_text())

    def finish(self):
        self.finish_button.click()
        return CheckoutCompletePage(self.page).expect_loaded()


class CheckoutCompletePage(BasePage):
    path = '/checkout-complete.html'

    def __init__(self, page):
        super().__init__(page)
        self.header = page.get_by_test_id('complete-header')
        self.back_home_button = page.get_by_test_id('back-to-products')

    def back_to_products(self):
        from pages.inventory_page import InventoryPage
        self.back_home_button.click()
        return InventoryPage(self.page).expect_loaded()
