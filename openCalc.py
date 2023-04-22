from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def openCalc():
    url = "https://aceship.github.io/AN-EN-Tags/akhr.html"
    browser = webdriver.Firefox()
    # open a new window if not already open

    browser.get(url)
    # select the element with attribute data-original-title="Caster"
    # wait 5 seconds for the element to be clickable
    sleep(5)
    element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-original-title='Caster']")))
    element.click()



