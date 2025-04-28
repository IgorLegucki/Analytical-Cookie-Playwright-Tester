import pytest
from playwright.sync_api import sync_playwright
from ing_cookie_test.ing_browser import click_customize_button, accept_selected_cookies, do_traffic_online

@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def test_accept_analytics_cookies(browser_name):
    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_name).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        click_customize_button(page)
        accept_selected_cookies(page)
        do_traffic_online(page)

        cookies = context.cookies()
        cookie_names = [c["name"] for c in cookies]
        print(f"[{browser_name}] Current cookies:", cookie_names)

        analytics_cookie_names = ["_ga", "_gid", "_gat", "SC_ANALYTICS_GLOBAL_COOKIE", "utma", "utmb", "AMCV", "AMCVS"]
        found = any(name in analytics_cookie_names for name in cookie_names)

        assert found, f"[{browser_name}] No analytical cookies found"

        browser.close()