import playwright
from playwright.sync_api import sync_playwright



@allure.title("A some test tile")
def test_dynamic_display_name():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
#     allure.dynamic.link("http://playwright.dev")
    page.goto("http://playwright.dev")
#     allure.dynamic.description("login to playwright site")
