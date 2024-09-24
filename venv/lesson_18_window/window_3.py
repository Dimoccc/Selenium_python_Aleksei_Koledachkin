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

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Получение дескриптора текущего окна
old_window = driver.current_window_handle
print("Дескриптор первого окна: ", old_window)

# Шаг 3 - Открытие и переключение на новое окно
driver.switch_to.new_window("window")

# Шаг 4 - Получение дескриптора нового окна
new_window = driver.current_window_handle
print("Дескриптор второго окна: ", new_window)

# Шаг 5 - Проверка, что окно переключилось
assert new_window == driver.current_window_handle, "Окно не переключилось"
time.sleep(2)

# Шаг 6 - Открытие страницы в новом окне
driver.get("https://vk.com")

# Шаг 7 - Переключение на старое окно
driver.switch_to.window(old_window)

# Шаг 8 - Проверка, что переключились на старое окно
assert old_window == driver.current_window_handle, "Окно не переключилось"

# Шаг 9 - Открытие страницы в старом окне
driver.get("https://ya.ru")

# Шаг 10 - Переключение на новое окно
driver.switch_to.window(new_window)

# Шаг 11 - Закрытие нового окна
driver.close()