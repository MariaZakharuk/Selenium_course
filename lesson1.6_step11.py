from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    first_name = browser.find_element_by_css_selector("div.first_block .form-control.first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element_by_css_selector("div.first_block .form-control.second")
    last_name.send_keys("Petrov")

    email = browser.find_element_by_css_selector("div.first_block .form-control.third")
    email.send_keys("name@mail.com")

    # Отправляем заполненную форму 
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
