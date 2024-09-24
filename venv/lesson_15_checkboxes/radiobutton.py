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

radio_yes_status = ('xpath', "//input[@id='yesRadio']")
radio_yes_click = ('xpath', "//label[@for='yesRadio']")

radio_no_status = ('xpath', "//input[@id='noRadio']")
radio_no_click = ('xpath',"//label[@for='noRadio']")

driver.get('https://demoqa.com/radio-button')

print(driver.find_element(*radio_yes_status).is_selected())
driver.find_element(*radio_yes_click).click()
print(driver.find_element(*radio_no_status).is_enabled())





