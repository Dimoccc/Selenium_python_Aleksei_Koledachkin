import time 
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
# options=options)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


driver.get('https://ya.ru/')

time.sleep(10)

driver.back()

time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()

time.sleep(3)