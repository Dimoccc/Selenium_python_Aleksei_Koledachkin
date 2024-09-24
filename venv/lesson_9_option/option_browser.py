import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options =webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")#без  интерфейса, объявляем до иницилизации драйвера
#chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата
chrome_options.add_argument("--window-size=1920,1080") 
chrome_options.add_argument("--disable-cache") 
chrome_options.page_load_strategy="eager"#normal standart


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options) 

#driver.set_window_size(700,700)

driver.get('https://whatismyipaddress.com/')

#driver.get('https://expired.badssl.com/')

time.sleep(3)