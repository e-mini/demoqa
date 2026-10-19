import re
from playwright.sync_api import Page, expect
from pathlib import Path


def test_text_box(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Text Box").click()

    page.locator("input[id='userName']").fill("Jamie Test")
    page.locator("input[id='userEmail']").fill("jtest@test.com")
    page.locator("textarea[id='currentAddress']").fill("123 Sesame St")
    page.locator("textarea[id='permanentAddress']").fill("123 Main St")
    page.locator("button[id='submit']").click()

    expect(page.locator("p[id=name]")).to_contain_text("Jamie Test")


def test_check_box(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Check Box").click()

    page.locator("span.rc-tree-checkbox").click()

    expect(page.locator("div[id='result']")).to_contain_text("downloads")
    expect(page.locator("div[id='result']")).to_contain_text("documents")
    expect(page.locator("div[id='result']")).to_contain_text("desktop")
#Assert that the one clicked is checked and the one not clicked is not checked

def test_radio_button(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Radio Button").click()

    page.locator("input[id='yesRadio']").click()
    expect(page.locator("span[class='text-success']")).to_contain_text("Yes")


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

    #expect() finish this assertion for homework - we are asserting on the row we added and asserting on all data added


def test_buttons(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Buttons").click()

    page.get_by_text("Click Me").nth(2).click()
    page.locator("button[id='doubleClickBtn']").dblclick()
    page.locator("button[id='rightClickBtn']").click(button="right")

    expect(page.get_by_text("You have done a double click")).to_be_visible()
    expect(page.get_by_text("You have done a right click")).to_be_visible()
    expect(page.get_by_text("You have done a dynamic click")).to_be_visible()
    

def test_links(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.locator("a[href='/links']").click()

    page.locator("a[id='simpleLink']").click()
    page.locator("a[id='dynamicLink']").click()
    
    page.locator("a[id='created']").click()
    expect(page.locator("p[id='linkResponse']")).to_contain_text("201")
    
    page.locator("a[id='no-content']").click()


    page.locator("a[id='moved']").click()


    page.locator("a[id='bad-request']").click()


    page.locator("a[id='unauthorized']").click()


    page.locator("a[id='forbidden']").click()


    page.locator("a[id='invalid-url']").click()

    #comeback to the ones where you must verify in a new tab


def test_broken_links(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.locator("a[href='/broken']").click()

    page.locator("a[href='http://demoqa.com']").click()
    expect(page.locator("img[class='banner-image']")).to_be_visible()

    page.go_back()
    page.locator("a[href='http://the-internet.herokuapp.com/status_codes/500']").click()
    expect(page.locator("h3")).to_contain_text("Status Codes", timeout=60000)

def test_download_and_upload(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.locator("a[href='/upload-download']").click()

    with page.expect_download() as albert:
        page.locator("a[id='downloadButton']").click()
    ben = albert.value
    ben.save_as("/Users/elise/code/demoqa/tests/support/" + ben.suggested_filename)
    file_path = Path("/Users/elise/code/demoqa/tests/support/" + ben.suggested_filename)
    assert file_path.exists()
    assert file_path.is_file()


    page.locator("input[id='uploadFile']").click()
    #skip upload and come back

def test_dynamic_properties(page):
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.locator("a[href='/dynamic-properties']").click()

    expect(page.get_by_text("This text has random Id")).to_be_visible()
    expect(page.locator("button[id='enableAfter']")).to_be_enabled(timeout=10000)
    page.locator("button[id='colorChange']").click()
    #skip asserting color change for now
    expect(page.locator("button[id='visibleAfter']")).to_be_visible()
