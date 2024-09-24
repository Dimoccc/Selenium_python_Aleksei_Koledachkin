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

driver.get("https://clipboardjs.com/")

SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")

SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)

action.scroll_to_element(SOME_ELEMENT).perform() # Используем скролл до элемента
time.sleep(3)