import os
import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_options =webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")#без  интерфейса, объявляем до иницилизации драйвера
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')

# chrome_options.accept_insecure_certs(True)

chrome_options.add_argument("--window-size=1080,720") 
#chrome_options.add_argument("--disable-cache") 
#chrome_options.page_load_strategy="normal"#normal - по стандарту, eager - без прогрузки картинок




service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options) 
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

visible_after_button = ("xpath","//button[@id='visibleAfter']")

wait.until(ec.visibility_of_all_elements_located(visible_after_button))
driver.find_element(*visible_after_button).click()
print('Кнопка нажата')
#river.find_element(*visible_after_button).click()


