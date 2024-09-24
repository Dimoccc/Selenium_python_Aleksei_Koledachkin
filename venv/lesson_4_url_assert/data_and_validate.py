import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) 

driver.get('https://www.wikipedia.org/')

url = driver.current_url
print('URL страницы', url)

current_title = driver.title
print('Текущий заголовок', current_title)

assert url == 'https://www.wikipedia.org/', 'Ошибка URL'
#assert url == 'https://www.wikipedia123.org/', 'Ошибка URL'
assert current_title == 'Wikipedia', 'Ошибка заголовка'


page_sourse = driver.page_source
print(page_sourse)

time.sleep(3)