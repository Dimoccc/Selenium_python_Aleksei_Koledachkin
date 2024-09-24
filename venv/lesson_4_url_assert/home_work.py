# Самостоятельная работа
# Инициализировать драйвер (любой, попробуйте Firefox) p.s: не забудьте его установить.
# Открыть любую страницу, например: vk.com.
# Получить и вывести title в консоль.
# Открыть любую другую страницу, например: ya.ru.
# Получить и вывести title в консоль.
# Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно.
# Сделать рефреш страницы.
# Получить и вывести URL-адрес текущей страницы.
# Вернуться "вперед" на страницу из пункта 4.
# Убедиться, что URL-адрес изменился.



import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) 

driver.get('https://vk.com/')

title_vk = driver.title
print('Текущий заголовок', title_vk)

time.sleep(3)

driver.get('https://www.youtube.com/')
title_youtube = driver.title
print('Текущий заголовок', title_youtube)
driver.back()
time.sleep(3)
assert  driver.title == title_vk, 'Не вернулись назад'

driver.refresh()
time.sleep(3)

url_vk = driver.current_url
print('Текущий URL', url_vk)
driver.forward()
print('Текущий URL', driver.current_url)
time.sleep(3)
assert driver.current_url != url_vk, 'Не сделали шаг вперед'
time.sleep(3)

