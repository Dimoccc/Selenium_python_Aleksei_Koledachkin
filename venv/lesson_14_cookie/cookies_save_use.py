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

# Переход на веб-страницу
driver.get("https://www.freeconferencecall.com/en/us/login")


#Сохранили куки и забили

# LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

# # Логинимся в аккаунт
# driver.get("https://www.freeconferencecall.com/en/us/login")
# driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("123")
# driver.find_element(*SUBMIT_BUTTON).click()

# pickle.dump(driver.get_cookies(),open(os.getcwd()+"\cookies.pkl","wb"))

driver.delete_all_cookies()

cookies =pickle.load(open(os.getcwd()+"\cookies.pkl","rb"))

for cook in cookies:
    driver.add_cookie(cook)

time.sleep(5)
driver.refresh()
time.sleep(5)