import pytest

from data import users
from pages.login_page import LoginPage


@pytest.fixture(scope='session', autouse=True)
def _use_data_test_attribute(playwright):
    """SauceDemo marks elements with data-test, not Playwright's default data-testid."""
    playwright.selectors.set_test_id_attribute('data-test')


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page).open()


@pytest.fixture
def inventory_page(login_page):
    """A browser already logged in as the standard user."""
    return login_page.login_as(users.STANDARD)
