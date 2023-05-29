
from selenium.webdriver.common.by import By



link = "https://stepik.org/lesson/236895/step/1"

browser.get(link)
browser.find_element(By.CLASS_NAME, "ember-view navbar__auth navbar__auth_login st-link st-link_style_button").clic()
time.sleep(3)
