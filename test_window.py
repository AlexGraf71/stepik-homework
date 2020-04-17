from selenium import webdriver
import time
import os
import math

link = " http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Opera()
    browser.get(link)
    browser.find_element_by_css_selector('[type="submit"]').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_name('text').send_keys(calc(x))
    browser.find_element_by_css_selector('[type="submit"]').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
