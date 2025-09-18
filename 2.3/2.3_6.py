import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math
import pyperclip

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем Submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

    # Переключение на другое окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Решаем задачку
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Вносим ответ в поле
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    # Нажимаем Submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

    # Копируем число в буфер обмена
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()