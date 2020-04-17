from selenium import webdriver
import time
import os
import math


link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Opera()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Ivan")
    browser.find_element_by_name("lastname").send_keys("Petrov")
    browser.find_element_by_name("email").send_keys("lexraf@list.ru")
    browser.find_element_by_css_selector('#file').send_keys(file_path)
    browser.send_keys(file_path)
    browser.find_element_by_css_selector('body > div.container > form > button').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

