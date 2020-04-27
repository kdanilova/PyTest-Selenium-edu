import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_parametrization(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1/"
    browser.get(link)
    input = browser.find_element_by_tag_name("textarea")
    answer = math.log(int(time.time()))
    input.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    feedback = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'smart-hints__hint'))
    )
    assert "Correct!" == feedback.text, "Feedback should be Correct!"
