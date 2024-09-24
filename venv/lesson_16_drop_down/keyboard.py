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

keybord = ("xpath", "//input[@id='target']")

driver.get('https://the-internet.herokuapp.com/key_presses')

driver.find_element(*keybord).send_keys(f"Hi, it's my{Keys.BACKSPACE}e")
driver.find_element(*keybord).send_keys(Keys.CONTROL + "A")
driver.find_element(*keybord).send_keys(Keys.BACKSPACE)