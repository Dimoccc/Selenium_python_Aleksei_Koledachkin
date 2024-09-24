import os
import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options =webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")#без  интерфейса, объявляем до иницилизации драйвера
#chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата

prefs = {
    "download.default_directory":f"{os.getcwd()}\downloads\lesson_6"
}

chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_argument("--window-size=1920,1080") 
chrome_options.add_argument("--disable-cache") 
chrome_options.page_load_strategy="normal"#normal - по стандарту, eager - без прогрузки картинок



service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options) 

driver.get('https://the-internet.herokuapp.com/download')
links = driver.find_elements("xpath","//div[@class = 'example']/a")
for i in links:
    # links = driver.find_elements("xpath","//li")
    time.sleep(2)
    i.click()
    print('Качаем файл', i) #,links.get_attribute("value")