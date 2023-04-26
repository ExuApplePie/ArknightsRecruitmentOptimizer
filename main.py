# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep

from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import pygetwindow
import getScreenshot
import getTags
import readTags
import keyboard
import os

def on_key_press(event):
    if event.name == '`':
        if (getScreenshot.getScreenshots() == -1):
            return  # if the emulator is not open terminate the program
        sleep(0.5)
        # this doesn't work
        browser.switch_to.window(browser.current_window_handle)
        # bring the browser to the front
        browser.maximize_window()
        getTags.createTags()
        tagList = readTags.getTagList()
        # deselect previously clicked tags
        try:
            (browser.find_element(By.CSS_SELECTOR, "button[onclick=\"clickBtnClear()\"]")).click()
            # iterate over tagList
            for i in tagList:
                print(f"[data-original-title='{i}']")
                element = (browser.find_element(By.CSS_SELECTOR, f"[data-original-title='{i}']"))
                element.click()
        except NoSuchElementException:
            print("NoSuchElementException")
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        except Exception as e:
            print(e)
    # exit if user inputs . key
    elif event.name == '.':
        browser.close()
        os._exit(0)
    elif event.name == '~':
        # show emulator
        try:
            win = pygetwindow.getWindowsWithTitle('arknights_emulator')[0]
            win.restore()
        except:
            print("Emulator not open")

def read_input():
    while True:
        print("Enter ` to select all tags, . to exit")
        keyboard.on_press(on_key_press)
        keyboard.wait() # this keeps the program running, probably not needed


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