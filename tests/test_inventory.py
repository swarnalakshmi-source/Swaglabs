import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage

BACKPACK = 'Sauce Labs Backpack'
BIKE_LIGHT = 'Sauce Labs Bike Light'


@pytest.mark.regression
def test_sort_by_price_low_to_high(inventory_page):
    inventory_page.sort_by(InventoryPage.SORT_PRICE_LOW_HIGH)
    prices = inventory_page.product_prices()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_by_name_z_to_a(inventory_page):
    inventory_page.sort_by(InventoryPage.SORT_NAME_ZA)
    names = inventory_page.product_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.smoke
def test_cart_badge_tracks_added_and_removed_items(inventory_page):
    inventory_page.add_to_cart(BACKPACK).add_to_cart(BIKE_LIGHT)
    expect(inventory_page.header.cart_badge).to_have_text('2')

    inventory_page.remove_from_cart(BIKE_LIGHT)
    expect(inventory_page.header.cart_badge).to_have_text('1')

    inventory_page.remove_from_cart(BACKPACK)
    expect(inventory_page.header.cart_badge).to_have_count(0)


def test_added_items_appear_in_cart(inventory_page):
    inventory_page.add_to_cart(BACKPACK).add_to_cart(BIKE_LIGHT)
    cart = inventory_page.open_cart()
    assert sorted(cart.product_names()) == sorted([BACKPACK, BIKE_LIGHT])
