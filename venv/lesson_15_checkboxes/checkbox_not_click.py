import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options =webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument("--window-size=1080,720")


# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://demoqa.com/checkbox')

checkbox_home_status = ("xpath", "//input[@id = 'tree-node-home']")
checkbox_home_click = ("xpath","//span[@class= 'rct-checkbox']")

print(driver.find_element(*checkbox_home_status).is_selected())
driver.find_element(*checkbox_home_click).click()
print(driver.find_element(*checkbox_home_status).is_selected())

time.sleep(3)