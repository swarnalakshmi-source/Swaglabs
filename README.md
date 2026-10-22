# SauceDemo - Page Object Model (Playwright + Python + pytest)

Target: https://www.saucedemo.com (public demo shop, demo credentials only).

## Structure
```
saucedemo-pom/
  pages/
    base_page.py            # shared base class
    login_page.py
    inventory_page.py
    cart_page.py
    checkout_page.py        # info, overview, complete pages
    components/header.py    # cart badge, menu, logout (on every page)
  data/users.py             # demo users and expected messages
  tests/                    # test_login, test_inventory, test_checkout
  conftest.py               # fixtures (login_page, inventory_page), data-test id config
  pytest.ini
  requirements.txt
```

## Setup and run
```
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                       # all tests
pytest -m smoke              # smoke only
pytest -n 4                  # parallel
pytest --headed              # watch the browser
pytest --browser firefox     # other browser (run: playwright install firefox)
```
Traces and screenshots for failures are kept in `test-results/`.
Open a trace with: `playwright show-trace test-results/<test>/trace.zip`.

## Conventions
- Locators live only in page objects; assertions live in tests.
- Page actions return the next page object, so tests read as user steps.
- SauceDemo uses the `data-test` attribute; `conftest.py` tells Playwright to use it for `get_by_test_id`.
