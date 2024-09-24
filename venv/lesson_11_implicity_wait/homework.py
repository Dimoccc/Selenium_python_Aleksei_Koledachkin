# Сайт для выполнения работы:
# https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver

# Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
# Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
# Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
# Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_options =webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument("--window-size=1080,720")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options) 
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")


text_field = ("xpath","//h2[@class='target-text']")
button_enamled =("xpath", "//button[@id ='hidden']")
button_activate = ("xpath", "//button[@id ='disable']")

driver.find_element("xpath","//button[@id ='populate-text']").click()

wait.until(ec.text_to_be_present_in_element(text_field,'Selenium Webdriver'),message="Текст не изменился на Selenium Webdriver")

driver.find_element("xpath","//button[@id ='display-other-button']").click()

wait.until(ec.element_to_be_clickable(button_enamled),message="Кнопка не появилась")

driver.find_element("xpath","//button[@id='enable-button']").click()
wait.until(ec.element_to_be_clickable(button_activate),message="Кнопка не появилась")

driver.find_element("xpath", "//button[@id='alert']").click()
wait.until(ec.alert_is_present())






