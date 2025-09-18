import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    name.send_keys('Иван')
    lastname.send_keys('Иван')
    email.send_keys('Иван')

    # Загружаем файл
    file = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'txt.txt')
    file.send_keys(file_path)

    # Нажимаем Submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()