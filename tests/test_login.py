import pytest
from playwright.sync_api import expect

from data import users
from data.users import Messages


@pytest.mark.smoke
def test_standard_user_can_log_in(login_page):
    inventory = login_page.login_as(users.STANDARD)
    expect(inventory.title).to_have_text('Products')
    expect(inventory.items).to_have_count(6)


def test_locked_out_user_is_rejected(login_page):
    login_page.login(users.LOCKED_OUT.username, users.LOCKED_OUT.password)
    expect(login_page.error).to_have_text(Messages.LOCKED_OUT)


@pytest.mark.parametrize('username, password, message', [
    ('', 'secret_sauce', Messages.USERNAME_REQUIRED),
    ('standard_user', '', Messages.PASSWORD_REQUIRED),
    ('standard_user', 'wrong_password', Messages.INVALID_CREDENTIALS),
    ('unknown_user', 'secret_sauce', Messages.INVALID_CREDENTIALS),
])
def test_invalid_login_shows_error(login_page, username, password, message):
    login_page.login(username, password)
    expect(login_page.error).to_have_text(message)


def test_user_can_log_out(inventory_page):
    login = inventory_page.header.logout()
    expect(login.login_button).to_be_visible()
