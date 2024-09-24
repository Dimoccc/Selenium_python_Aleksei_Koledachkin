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

driver.get("https://demoqa.com/buttons")

OUTLINE_BUTTON_LOCATOR = ("xpath", "//button[text() = 'Click Me']")
text_after_click_and_hold= ("xpath", "//div//p[@id = 'dynamicClickMessage']")

BUTTON = driver.find_element(*OUTLINE_BUTTON_LOCATOR)

action.click_and_hold(BUTTON).pause(2).release().perform()
# wait.until(EC.presence_of_element_located(text_after_click_and_hold))


print(driver.find_element(*text_after_click_and_hold).text)