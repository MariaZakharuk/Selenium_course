from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("treasure")
    x_value = x_element.get_attribute("valuex")
    y = calc(x_value)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
