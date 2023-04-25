from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import threading

import getScreenshot
import getTags
import readTags

url = "https://aceship.github.io/AN-EN-Tags/akhr.html"
browser = webdriver.Firefox()
# open a new window if not already open
browser.get(url)

def read_input():
    oldTagList = []
    while True:
        print("Enter ` to select all tags, \\ to exit")
        user_input = input()
        # check if user inputted ` key
        if user_input == '`':
            getScreenshot.getScreenshot()
            getTags.createTags()
            tagList = readTags.getTags()
            # deselect previously clicked tags
            if oldTagList != []:
                for i in oldTagList:
                    element = (browser.find_element(By.CSS_SELECTOR, f"[data-original-title='{i}']"))
                    element.click()
            oldTagList = tagList
            # iterate over tagList
            for i in tagList:
                print(f"[data-original-title='{i}']")
                element = (browser.find_element(By.CSS_SELECTOR, f"[data-original-title='{i}']"))
                element.click()
        # exit if user inputs \ key
        elif user_input == '\\':
            break

def openCalc():
    # select the element with attribute data-original-title="Caster"
    # wait 5 seconds for the element to be clickable, caster chosen arbitrarily
    sleep(5)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-original-title='Caster']")))
    (browser.find_element(By.CSS_SELECTOR, "#navitemRegion > #regionDropdown")).click()
    # wait a tiny bit for the dropdown to appear
    sleep(0.1)
    (browser.find_element(By.CSS_SELECTOR, "[value='en']")).click()
    input_thread = threading.Thread(target=read_input)
    input_thread.start()
    input_thread.join()



