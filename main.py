import os
from time import sleep

import keyboard
from pywinauto import application
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import const
import getScreenshot
import readTags

app = application.Application()
app2 = application.Application()
try:
    app.connect(title_re=const.EMULATOR_NAME)
except:
    print("Emulator not open")


def on_key_press(event):
    if event.name == const.INPUT_TAG_KEY:
        if (getScreenshot.get_screenshot() == -1):
            return  # if the emulator is not open terminate the program
        sleep(0.1)
        # bring the browser to the front
        app2.top_window().set_focus()
        tagList = readTags.get_tag_list()
        # deselect previously clicked tags
        try:
            (browser.find_element(By.CSS_SELECTOR, "button[onclick=\"clickBtnClear()\"]")).click()
            # iterate over tagList
            for i in tagList:
                element = (browser.find_element(By.CSS_SELECTOR, f"[data-original-title='{i}']"))
                element.click()
        except NoSuchElementException:
            print("NoSuchElementException")
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        except Exception as e:
            print(e)
    # exit if user inputs . key
    elif event.name == const.END_PROGRAM_KEY:
        browser.close()
        os._exit(1)
    elif event.name == const.SHOW_EMULATOR_KEY:
        # show emulator
        try:
            # set focus
            app.top_window().set_focus()
        except:
            print("Emulator not open")


def read_input():
    while True:
        print(
            f"Enter {const.INPUT_TAG_KEY} to select all tags, {const.SHOW_EMULATOR_KEY} to return to emulator {const.END_PROGRAM_KEY} to exit")
        keyboard.on_press(on_key_press)
        keyboard.wait()  # this keeps the program running, probably not needed


def openCalc():
    # select the element with attribute data-original-title="Caster"
    # wait 5 seconds for the element to be clickable, caster chosen arbitrarily
    sleep(3)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-original-title='Caster']")))
    (browser.find_element(By.CSS_SELECTOR, "#navitemRegion > #regionDropdown")).click()
    # wait a tiny bit for the dropdown to appear
    sleep(0.1)
    (browser.find_element(By.CSS_SELECTOR, "[value='en']")).click()


if __name__ == '__main__':
    url = "https://aceship.github.io/AN-EN-Tags/akhr.html"
    browser = webdriver.Firefox()
    # open a new window if not already open
    browser.get(url)
    app2.connect(title_re=browser.title)
    openCalc()
    read_input()
