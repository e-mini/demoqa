import re
from playwright.sync_api import Page, expect


def test_text_box(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Text Box").click()

    page.locator("input[id='userName']").fill("Jamie Test")
    page.locator("input[id='userEmail']").fill("jtest@test.com")
    page.locator("textarea[id='currentAddress']").fill("123 Sesame St")
    page.locator("textarea[id='permanentAddress']").fill("123 Main St")
    page.locator("button[id='submit']").click()


def test_check_box(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Check Box").click()

    page.locator("span.rc-tree-checkbox").click()


def test_radio_button(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Radio Button").click()

    page.locator("input[id='yesRadio']").click()


def test_web_tables(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Web Tables").click()

    page.locator("button[id='addNewRecordButton']").click()
    page.locator("input[id='firstName']").fill("Jamie")
    page.locator("input[id='lastName']").fill("Test")
    page.locator("input[id='userEmail']").fill("jtest@test.com")
    page.locator("input[id='age']").fill("25")
    page.locator("input[id='salary']").fill("1000000")
    page.locator("input[id='department']").fill("Development")
    page.locator("button[id='submit']").click()


def test_buttons(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Buttons").click()

    page.get_by_text("Click Me").click
    page.locator("button[id='doubleClickBtn']").dblclick()
    page.locator("button[id='rightClickBtn']").click(button="right")

def test_links(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.locator("a[href='/links']").click()

    page.locator("a[id='simpleLink']").click()
    page.locator("a[id='dynamicLink']").click()
    page.locator("a[id='created']").click()
    page.locator("a[id='no-content']").click()
    page.locator("a[id='moved']").click()
    page.locator("a[id='bad-request']").click()
    page.locator("a[id='unauthorized']").click()
    page.locator("a[id='forbidden']").click()
    page.locator("a[id='invalid-url']").click