from selenium import webdriver
import time
import unittest

link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)


class TestRegistration(unittest.TestCase):
    def test_abs1(self):
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys("Ivan")
        browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys("Ivan")
        browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys("Ivan")
        browser.find_element_by_class_name("second").send_keys("Ivan")
        browser.find_element_by_class_name("third").send_keys("Ivan")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    def test_abs2(self):
        browser.get(link2)
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys("Ivan")
        browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys("Ivan")
        browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys("Ivan")
        browser.find_element_by_class_name("second").send_keys("Ivan")
        browser.find_element_by_class_name("third").send_keys("Ivan")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text


if __name__ == "__main__":
    unittest.main()