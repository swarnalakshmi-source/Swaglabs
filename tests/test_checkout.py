import pytest
from playwright.sync_api import expect

from data.users import Messages

BACKPACK = 'Sauce Labs Backpack'
ONESIE = 'Sauce Labs Onesie'


@pytest.mark.smoke
def test_user_can_complete_checkout(inventory_page):
    inventory_page.add_to_cart(BACKPACK).add_to_cart(ONESIE)

    cart = inventory_page.open_cart()
    info = cart.checkout()
    overview = info.fill_information('Asha', 'Kumar', '641001').continue_to_overview()

    assert sorted(overview.product_names()) == sorted([BACKPACK, ONESIE])
    assert overview.total() == pytest.approx(overview.subtotal() + overview.tax())

    complete = overview.finish()
    expect(complete.header).to_have_text(Messages.ORDER_COMPLETE)

    inventory = complete.back_to_products()
    expect(inventory.header.cart_badge).to_have_count(0)


@pytest.mark.regression
@pytest.mark.parametrize('first, last, postal, message', [
    ('', 'Kumar', '641001', Messages.FIRST_NAME_REQUIRED),
    ('Asha', '', '641001', 'Error: Last Name is required'),
    ('Asha', 'Kumar', '', 'Error: Postal Code is required'),
])
def test_checkout_information_is_validated(inventory_page, first, last, postal, message):
    inventory_page.add_to_cart(BACKPACK)
    info = inventory_page.open_cart().checkout()
    info.fill_information(first, last, postal).submit()
    expect(info.error).to_have_text(message)
