# Самостоятельная работа
# Задание 1:

# Заполнить все текстовые поля данными (почистить поля перед заполнением).
# Проверить, что данные действительно введены, используя get_attribute() и assert.
# Страница для выполнения задания: https://demoqa.com/text-box
 

# Задание 2:

# Прокликать все ссылки со статус-кодами на странице, используя алгоритм перебора элементов.
# После каждого клика возвращаться на стартовую страницу.
# Страница для выполнения задания: http://the-internet.herokuapp.com/status_codes

import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) 

driver.get('https://demoqa.com/text-box')

full_name = driver.find_element("xpath","//input[@id='userName']")
full_name.clear()
send_full_name = 'ABOBA BOBA'
full_name.send_keys(send_full_name)
#assert send_full_name==full_name.get_attribute(), 'Введеное full name в поле не соответствует отправленным данным'
print(full_name,send_full_name)

email = driver.find_element("xpath", "//input[@type ='email']")
email.clear()
send_email = 'ddimocmb@gmail.com'
email.send_keys(send_email)
assert send_email==email.get_attribute('value'), 'Введеный email в поле не соответствует отправленным данным'
print(email,send_email)

current_adress = driver.find_element("xpath","//textarea[@placeholder='Current Address']")
current_adress.clear()
send_current_adress = 'Москва ул. Пупкина'
current_adress.send_keys(send_current_adress)
assert send_current_adress==current_adress.get_attribute('value'), 'Введеный adress в поле не соответствует отправленным данным'
print(current_adress,send_current_adress)

parmanent_adress= driver.find_element("xpath","//textarea[@id='permanentAddress']")
parmanent_adress.clear()
send_parmanent_adress = 'Уфа ул. Ленивая'
parmanent_adress.send_keys(send_parmanent_adress)
assert send_parmanent_adress==parmanent_adress.get_attribute('value'), 'Введеный adress в поле не соответствует отправленным данным'
print(parmanent_adress,send_parmanent_adress)

time.sleep(5)

driver.get('https://the-internet.herokuapp.com/status_codes')
links = driver.find_elements("xpath","//li/a")
for i in links:
    # links = driver.find_elements("xpath","//li")
    i.click()
    print(driver.current_url)
    time.sleep(2)
    driver.back()
    time.sleep(2)

