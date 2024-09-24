import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options =Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument("--window-size=1080,720")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

service = Service(executable_path=ChromeDriverManager().install())


user_1 = webdriver.Chrome(service=service,options=chrome_options)
wait = WebDriverWait(user_1, 10, poll_frequency=1)



login = ("xpath", "//input[@type ='email']")
password = ("xpath", "//input[@type = 'password']")
submit = ("xpath", "//button[@type = 'submit']")

user_1.get("https://hyperskill.org/login")
wait.until(EC.element_to_be_clickable(submit))
user_1.find_element(*login).send_keys("alekseik@ya.ru")
user_1.find_element(*password).send_keys("Qwerty132!")
user_1.find_element(*submit).click()
time.sleep(2)

user_2 = webdriver.Chrome(service=service,options=chrome_options)
user_2.get("https://hyperskill.org/login")
