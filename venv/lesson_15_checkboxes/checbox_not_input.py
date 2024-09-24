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

driver.get('https://demoqa.com/selectable')

element_one = ("xpath", "//li[text()= 'Cras justo odio']")

before = driver.find_element(*element_one).get_attribute('class')
print(driver.find_element(*element_one).get_attribute('class'))

driver.find_element(*element_one).click()

after = driver.find_element(*element_one).get_attribute('class')
print(after)
assert 'active' in after

time.sleep(3)