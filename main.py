import sys
from time import sleep

from playwright.sync_api import sync_playwright, expect

import keyboard
from pywinauto import application


import const
import getScreenshot
import readTags

import queue

key_queue = queue.Queue()

app = application.Application()
app2 = application.Application()
try:
    app.connect(title_re=const.EMULATOR_NAME)
except:
    print("Emulator not open")


def on_key_press(event):
    if event.name == const.INPUT_TAG_KEY:
        key_queue.put("input_tags")
    elif event.name == const.END_PROGRAM_KEY:
        key_queue.put("exit")
    elif event.name == const.SHOW_EMULATOR_KEY:
        key_queue.put("show_emulator")

def handle_key_actions(browser, page):
    if (getScreenshot.get_screenshot() == -1):
        return  # if the emulator is not open terminate the program
    expect(page.get_by_text("Reset")).to_be_visible(timeout=5000)  # wait for the page to load
    page.get_by_text("Reset").click()  # reset the page to clear previous tags
    # bring the browser to the front
    app2.top_window().set_focus()
    tagList = readTags.get_tag_list()
    # deselect previously clicked tags
    try:
        for i in tagList:
            page.get_by_text(i, exact=True).click()
        page.locator("#recruitResults").scroll_into_view_if_needed()
    except Exception as e:
        print(e)

def read_input(browser, page):
    keyboard.on_press(on_key_press)
    while True:
        try:
            action = key_queue.get(timeout=0.1)
            if action == "input_tags":
                handle_key_actions(browser, page)
            elif action == "exit":
                browser.close()
                sys.exit()
            elif action == "show_emulator":
                try:
                    app.top_window().set_focus()
                except:
                    print("Emulator not open")
        except queue.Empty:
            pass
        # print(
        #     f"Enter {const.INPUT_TAG_KEY} to select all tags, {const.SHOW_EMULATOR_KEY} to return to emulator {const.END_PROGRAM_KEY} to exit")
        # keyboard.on_press(lambda event: on_key_press(event, browser, page))
        # keyboard.wait()  # this keeps the program running, probably not needed



if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={ 'width': 1920, 'height': 1080 })
        page = context.new_page()
        page.goto(const.WEBSITE)
        app2.connect(title_re=page.title(), found_index=0)  # test which found index works
        read_input(browser=browser, page=page)
