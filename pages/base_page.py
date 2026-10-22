from playwright.sync_api import Page, expect


class BasePage:
    """Shared behaviour for every page object.

    Rules: locators live in page objects only; test files decide what is correct
    (assertions), page objects only describe the screen and what a user can do.
    """

    path = '/'

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.path)
        return self

    def expect_loaded(self):
        """Light 'am I on the right page' check used after navigation."""
        expect(self.page).to_have_url(f'**{self.path}')
        return self
