import pytest
from selenium.webdriver.common.by import By
import time
import math

def calc():
    return str(math.log(int(time.time())))

@pytest.mark.parametrize('number', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/236{number}/step/1?auth=login"
    browser.get(link)
    time.sleep(8)
    login_input = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
    login_input.send_keys("ma")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    password_input.send_keys("9")
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(5)
    answerino = browser.find_element(By.CSS_SELECTOR, "textarea")
    answerino.send_keys(calc())
    answerino_button = browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']")
    answerino_button.click()
    time.sleep(2)
    hint = browser.find_element(By.CSS_SELECTOR, "p[class='smart-hints__hint']")
    hint_text = hint.text
    print(hint_text)
    assert "Correct!" == hint_text





