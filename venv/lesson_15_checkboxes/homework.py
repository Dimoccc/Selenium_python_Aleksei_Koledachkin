import random
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

block_buttons = ("xpath","//div[@id='demo-tabpane-grid']//li")
grid = ("xpath", "//a[@id = 'demo-tab-grid']")

driver.get('https://demoqa.com/selectable')

driver.find_element(*grid).click()
random_one= random.choice(driver.find_elements(*block_buttons))
random_one.click()

random_two = random.choice(driver.find_elements(*block_buttons))

random_two.click()

after_one = random_one.get_attribute('class')
after_two = random_two.get_attribute('class')

assert 'active' in after_one
assert 'active' in after_two

time.sleep(10)

print(random_one)

print(random_two)


