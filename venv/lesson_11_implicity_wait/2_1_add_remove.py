import os
import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_options =webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument("--window-size=1080,720")


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options) 
wait = WebDriverWait(driver, 15, poll_frequency=1)

# Тест 1 нажимаем ждем чтоб после нажатия кнопка исчезла
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# remove_button =("xpath","//button[text()='Remove']")

# driver.find_element(*remove_button).click()
# wait.until(ec.invisibility_of_element_located(remove_button))

# print('Ok')


# ожидание кликабильности кнопок, отправка текста и вывод ок
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

enamle_button = ("xpath", "//button[text() = 'Enable']")
text_field = ("xpath", "//input[@type = 'text']")

wait.until(ec.element_to_be_clickable(enamle_button)).click()
wait.until(ec.element_to_be_clickable(text_field)).send_keys("Hello")
wait.until(ec.text_to_be_present_in_element_value(text_field, "Hello"))

print("Ok")


