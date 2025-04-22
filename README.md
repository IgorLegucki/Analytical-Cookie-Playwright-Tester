# Analytics Cookie Consent Tester

This project is an automated test suite that verifies whether analytical cookies are correctly set after enabling consent on the ING Poland website. It uses [Microsoft Playwright](https://playwright.dev/python/) and [Pytest](https://docs.pytest.org/) to simulate user interactions and monitor cookies and network requests.

## Features

- Clicks the consent toggle for analytical cookies
- Confirms settings by pressing "Accept selected"
- Navigates to a target subpage to trigger tracking scripts
- Verifies the presence of analytical cookies like `_ga`, `AMCV_`, or `s_cc`

## Tech Stack

- Python 3.10+
- Playwright (sync API)
- Pytest

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/analytics-cookie-consent-tester.git
cd analytics-cookie-consent-tester
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

## Running Tests
To run the cookie consent test and see browser output:

```bash
pytest -s tests/test_cookies.py
```
-s is required for proper stdin/output behavior during debugging.

## Project Structure

```bash
├── .github/
│   └── workflows
│       └── tests.yml
├── ing_cookie_test/
│   └── ing_browser.py 
├── tests/
│   └── test_cookies.py
├── README.md
├── .gitignore
├── requirements.txt
```

## Notes
The test assumes that the cookie consent UI is immediately visible after page load.

You can change the target page (used to trigger scripts) via page.goto(...) in the test file.

Headless mode is disabled for better debugging.
