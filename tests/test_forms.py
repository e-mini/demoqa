import re
from playwright.sync_api import Page, expect

def test_practice_form(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Forms").click()

    page.
   
