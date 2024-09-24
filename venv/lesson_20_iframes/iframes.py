#Сайт без iframe, не работает(
#Перенабираем код чтоб запомнить

import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options =Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument("--window-size=1080,720")

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://demoqa.com/nestedframes")

time.sleep(3)
driver.switch_to.frame("frame1")
print(driver.find_element("xpath", "//body").text)

driver.switch_to.frame(0)
print(driver.find_element("xpath", "//body").text)
driver.switch_to.parent_frame()
print(driver.find_element("xpath", "//body").text)

driver.switch_to.default_content()
print(driver.find_element("xpath", "//body").text)
