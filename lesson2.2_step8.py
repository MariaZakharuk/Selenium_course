import os 
from selenium import webdriver
import time

with open('test1.txt', 'w') as file:
   file.write('random text')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("div>input:nth-child(2)[required]")
    first_name.send_keys('Ivan')

    last_name = browser.find_element_by_css_selector("div>input:nth-child(4)[required]")
    last_name.send_keys('Petrov')

    email = browser.find_element_by_css_selector("div>input:nth-child(6)[required]")
    email.send_keys('name@mail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    path = os.getcwd() + '/' + file.name  # Вариант получать путь из только что созданного файла

    element = browser.find_element_by_id("file")
    element.send_keys(path) # Или element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
