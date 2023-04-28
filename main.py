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
import getTags
import readTags

app = application.Application()
app.connect(title_re=const.emulator_name)


def on_key_press(event):
    if event.name == const.input_tag_key:
        if (getScreenshot.get_screenshot() == -1):
            return  # if the emulator is not open terminate the program
        sleep(0.1)
        # bring the browser to the front
        browser.maximize_window()
        getTags.createTags()
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
    elif event.name == const.input_tag_key3:
        browser.close()
        os._exit(0)
    elif event.name == const.input_tag_key2:
        # show emulator
        try:
            # set focus
            app.top_window().set_focus()
        except:
            print("Emulator not open")


def read_input():
    while True:
        print(
            f"Enter {const.input_tag_key} to select all tags, {const.input_tag_key2} to return to emulator {const.input_tag_key3} to exit")
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
    openCalc()
    read_input()
    # disconnect from the emulator
    app.kill()
