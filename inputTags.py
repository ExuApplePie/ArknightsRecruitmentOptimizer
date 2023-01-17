from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://aceship.github.io/AN-EN-Tags/akhr.html")
delay = 5
try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'unselectable'))
    WebDriverWait(driver, delay).until(element_present)
except TimeoutException:
    print("Loading took too much time!")
button = driver.find_elements(By.CLASS_NAME, "unselectable")[1]
button.click()
# document.getElementsByClassName("unselectable")[1].click()