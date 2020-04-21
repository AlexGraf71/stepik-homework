import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

testdata = ['https://stepik.org/lesson/236895/step/1',
            'https://stepik.org/lesson/236896/step/1',
            'https://stepik.org/lesson/236897/step/1',
            'https://stepik.org/lesson/236898/step/1',
            'https://stepik.org/lesson/236899/step/1',
            'https://stepik.org/lesson/236903/step/1',
            'https://stepik.org/lesson/236904/step/1',
            'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', testdata)
def test_parametrize_test(browser, url):
    answer = math.log(int(time.time()))
    browser.get(url)
    WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CLASS_NAME, "textarea"))
    )
    browser.find_element_by_css_selector('.textarea').click()
    browser.find_element_by_css_selector('.textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission').click()
    WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    assert browser.find_element_by_css_selector('.smart-hints__hint').text == 'Correct!'



