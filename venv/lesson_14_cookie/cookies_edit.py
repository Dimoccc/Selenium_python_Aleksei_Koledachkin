import time

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

# Переход на веб-страницу
driver.get("https://www.freeconferencecall.com/en/us/login")

# 1 кук

# before = driver.get_cookie("split")
# print(before)
# driver.delete_cookie("split")

# driver.add_cookie({
#     "name": "split",
#     "value": "TestAboba"
# })

# after = driver.get_cookie('split')
# print(after)

# Все куки

before = driver.get_cookies()
print(before)
driver.delete_all_cookies()

driver.add_cookie({
    "name": "split",
    "value": "TestAboba"
})

after = driver.get_cookie('split')
print(after)
