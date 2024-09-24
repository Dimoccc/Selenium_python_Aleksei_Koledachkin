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

driver.get("https://tympanus.net/Development/DragDropInteractions/page-scale.html")
locator_a = ("xpath", "//div[@class='grid__item'][1]")
locator_b = ("xpath", "//div[@class='drop-area__item'][1]")

# JavaScript stop - setTimeout(function() { debugger; }, 5000);

a = driver.find_element(*locator_a)
# b = driver.find_element(*locator_b)

action.click_and_hold(a).pause(2).move_to_element(driver.find_element(*locator_b)).release().perform()
time.sleep(3)