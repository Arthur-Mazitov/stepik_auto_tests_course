import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем Submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

    # Нажимаем на кнопку на всплывающем окне
    confirm = browser.switch_to.alert
    confirm.accept()

    # Решаем задачку
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Вносим ответ в поле
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    # Нажимаем Submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()