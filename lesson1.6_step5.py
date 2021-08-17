from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    text_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

    browser = webdriver.Chrome()
    browser.get(link)

    link1 = browser.find_element_by_link_text(text_link)
    link1.click()

    сin1 = browser.find_element_by_tag_name("input")
    сin1.send_keys("Ivan")
    сin2 = browser.find_element_by_name("last_name")
    сin2.send_keys("Petrov")
    сin3 = browser.find_element_by_class_name("city")
    сin3.send_keys("Smolensk")
    сin4 = browser.find_element_by_id("country")
    сin4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
