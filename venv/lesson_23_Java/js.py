import time
from lesson_23_Java.scrolls import Scrolls 

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
scrolls = Scrolls(driver,action)

driver.get("https://seiyria.com/bootstrap-slider/")

ex_2_locator = ("xpath","//h3[text()='Example 2: ']" )
ex_2 = driver.find_element(*ex_2_locator)

scrolls.scroll_to_element(ex_2)

time.sleep(2)