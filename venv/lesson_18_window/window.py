import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
# клавиатура
#from selenium.webdriver import Keys

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
#wait = WebDriverWait(driver, 10, poll_frequency=1)
 
for_business_button_locator= ("xpath", "//a[text()=' For Business ']")
star_for_free_button = ("xpath", "(//a[text()='Start for Free'])[1]")

driver.get("https://hyperskill.org/tracks")

#инфа по активному окну
# print(driver.current_window_handle)

#Все окна
#print(driver.window_handles)

driver.find_element(*for_business_button_locator).click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

driver.find_element(*star_for_free_button).click()

time.sleep(5)