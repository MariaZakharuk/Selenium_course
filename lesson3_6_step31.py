from selenium import webdriver
import math
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236897/step/1/"
browser = webdriver.Chrome()
browser.get(link)

#def calc():
#    return str(math.log(int(time.time())))

a = math.log(int(time.time()))

print(f"a = {a}")
#b = a.text
try:
    browser.implicitly_wait(5)
    answer = browser.find_element_by_css_selector(".ember-text-area")
    answer.send_keys(str(a))
   # btn = WebDriverWait(browser, 12).until(
   #     EC.element_to_be_clickable(By.CSS_SELECTOR, ".submit-submission")
   # )
    btn = browser.find_element_by_css_selector(".submit-submission")
    time.sleep(1)
    btn.click()

    #print(browser.switch_to.alert.text)

finally:
    time.sleep(10)
    #browser.quit()
