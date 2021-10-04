import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

#class Test_test(object):    
num = ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"]
#msg=""
@pytest.mark.parametrize('num', num)
def test_guest_should_add_answer (browser, num):
    link = f"https://stepik.org/lesson/{num}/"
    browser.get(link)
    time.sleep(3)
    #browser.implicity_wait(10)
    answer = browser.find_element_by_css_selector(".ember-text-area")
    a = math.log(int(time.time()))
    answer.send_keys(str(a))

    btn = browser.find_element_by_css_selector(".submit-submission")
    time.sleep(1)
    btn.click()
    time.sleep(1)
    resp = browser.find_element_by_css_selector(".smart-hints__hint")
    resp.text
    print(resp.text)

    #if resp!="Correct!":
     #   msg=msg+resp
        #print(msg)

if __name__ == "__main__":
    unittest.main()

#answer = math.log(int(time.time()))
#print(answer)