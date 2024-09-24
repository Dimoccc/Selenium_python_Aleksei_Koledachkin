import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
# клавиатура
#from selenium.webdriver import Keys

chrome_options =webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument("--window-size=1080,720")


# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)
#wait = WebDriverWait(driver, 10, poll_frequency=1)
 


# #driver.get("https://hyperskill.org/tracks")

# driver.switch_to.new_window("tab")
# time.sleep(5)

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Открытие нескольких вкладок
driver.switch_to.new_window('tab')
driver.switch_to.new_window('tab')
time.sleep(2)

# Шаг 3 - Получение списка открытых вкладок
windows = driver.window_handles
print(len(windows)) # Выведем на экран кол-во открытых вкладок

# Шаг 4 - Получение дескриптора текущего окна для дальнейшей проверки
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)
print("Индекс: ", windows.index(current_tab)) # Получаем индекс вкладки в списке для информативности

# Шаг 5 - Переключение на вкладку по ее индексу
driver.switch_to.window(windows[1])
time.sleep(2)

# Шаг 6 - Проверка, что вкладка переключилась
assert current_tab != driver.current_window_handle, "Вкладка не переключилась"