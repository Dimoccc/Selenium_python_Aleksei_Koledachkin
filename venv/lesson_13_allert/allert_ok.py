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

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")

# Клик на кнопку, которая вызывает alert
BUTTON_1 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()

# Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
alert = wait.until(EC.alert_is_present())

# Переключение на alert
driver.switch_to.alert

allert = wait.until(EC.alert_is_present())
driver._switch_to.alert

time.sleep(3)

allert.accept

time.sleep(3)