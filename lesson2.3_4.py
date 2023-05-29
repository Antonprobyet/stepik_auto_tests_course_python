from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    i0_click_button = browser.find_element(By.XPATH, "//button[normalize-space()='I want to go on a magical journey!']").click()
    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1_add_answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    input4 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()