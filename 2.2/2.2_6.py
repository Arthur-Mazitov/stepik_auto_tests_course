import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Заполняем input
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(str(y))

    # Заполняем checkbox
    checkbox = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox.click()

    # Заполняем radiobutton
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobutton.click()

    # Нажимаем Submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()