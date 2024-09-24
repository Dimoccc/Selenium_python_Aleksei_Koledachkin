import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# class select dropdown
from selenium.webdriver.support.select import Select

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

select_locator = ("xpath", "//select[@id='dropdown']")

driver.get('https://the-internet.herokuapp.com/dropdown')

dropdown = Select(driver.find_element(*select_locator))

# Нажатие по атрибутам

# dropdown.select_by_visible_text("Option 1")
# dropdown.select_by_value("1")
# dropdown.select_by_index("1")

all_options = dropdown.options

# for option in all_options:
#     dropdown.select_by_visible_text(option.text)
#     if 'Option 1' in option.text:
#         print("Опция есть")

# for option in all_options:
#     dropdown.select_by_index(all_options.index(option))

for option in all_options:
    dropdown.select_by_value(option.get_attribute('value'))

time.sleep(3)


