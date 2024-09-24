import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1) # Создаем обьект ожиданий
action = ActionChains(driver) # Создаем обьект action

driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(3)
locator_squre_a = ("xpath", "//div[@id='column-a']")
locator_squre_b = ("xpath", "//div[@id='column-b']")

squre_a = driver.find_element(*locator_squre_a)
squre_b = driver.find_element(*locator_squre_b)

action.drag_and_drop(squre_a, squre_b).perform()
time.sleep(3)