import playwright
from playwright.sync_api import sync_playwright



def test_dynamic_display_name():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print("test is completed")
   
