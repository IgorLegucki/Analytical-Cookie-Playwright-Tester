from playwright.sync_api import Page

def click_customize_button(page: Page):
    page.goto("https://www.ing.pl")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector('button.js-cookie-policy-main-settings-button', timeout=60000)
    page.click('button.js-cookie-policy-main-settings-button')

def accept_selected_cookies(page: Page):
    page.wait_for_selector('div.cookie-policy-toggle-button[name="CpmAnalyticalOption"]', timeout=60000)

    toggle = page.query_selector('div.cookie-policy-toggle-button[name="CpmAnalyticalOption"]')
    if toggle.get_attribute("aria-checked") == "false":
        toggle.click()

    page.wait_for_selector('button.js-cookie-policy-settings-decline-button', timeout=60000)
    page.click('button.js-cookie-policy-settings-decline-button')

def do_traffic_online(page: Page):
    page.goto("https://www.ing.pl/indywidualni/kredyty-i-pozyczki")
    page.wait_for_load_state('networkidle')
