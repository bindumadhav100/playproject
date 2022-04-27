import playwright
from playwright.sync_api import sync_playwright
import allure



def test_dynamic_display_name():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    allure.dynamic.link("http://playwright.dev")
    page.goto("http://playwright.dev")
    print("test is completed")
    allure.dynamic.description("login to playwright site")
