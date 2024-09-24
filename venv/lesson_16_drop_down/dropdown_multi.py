import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# клавиатура
from selenium.webdriver import Keys

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

multiselect_locator = ("xpath", "//input[@id='react-select-4-input']")

driver.get('https://demoqa.com/select-menu')

driver.find_element(*multiselect_locator).send_keys("Green")
driver.find_element(*multiselect_locator).send_keys(Keys.ENTER)

driver.find_element(*multiselect_locator).send_keys("Black")
driver.find_element(*multiselect_locator).send_keys(Keys.ENTER)




