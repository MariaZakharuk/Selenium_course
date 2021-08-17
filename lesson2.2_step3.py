from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_id("num1").text
    y_element = browser.find_element_by_id("num2").text
    z = int(x_element) + int(y_element)
    
    select = Select(browser.find_element_by_tag_name("select"))
    answer = select.select_by_value(str(z))
   # answer.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
