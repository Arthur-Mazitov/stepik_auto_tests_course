import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        add_name = browser.find_element(By.CSS_SELECTOR, "div[class='first_block']>:nth-child(1)>input[class='form-control first']")
        add_name.send_keys("Ivan")
        add_surname = browser.find_element(By.CSS_SELECTOR, "div[class='first_block']>:nth-child(2)>input[class='form-control second']")
        add_surname.send_keys("Ivan")
        add_email = browser.find_element(By.CSS_SELECTOR, "div[class='first_block']>:nth-child(3)>input[class='form-control third']")
        add_email.send_keys("Ivan")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        add_name = browser.find_element(By.CSS_SELECTOR, "div[class='first_block']>:nth-child(1)>input[class='form-control first']")
        add_name.send_keys("Ivan")
        add_surname = browser.find_element(By.CSS_SELECTOR, "div[class='first_block']>:nth-child(2)>input[class='form-control second']")
        add_surname.send_keys("Ivan")
        add_email = browser.find_element(By.CSS_SELECTOR, "div[class='first_block']>:nth-child(3)>input[class='form-control third']")
        add_email.send_keys("Ivan")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()