#194.8.233.243

import time
from selenium import webdriver

PROXY = "http://proxy-srv.rgslife.local:3128" # Указываем адрес прокси-сервера
#PROXY = "username:password@37.19.220.129:8443"
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXY}") # Добавляем прокси через опции

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://2ip.ru") # Проверяем IP-адрес

time.sleep(5)