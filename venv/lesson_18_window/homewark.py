import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# клавиатура
#from selenium.webdriver import Keys

chrome_options =webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors") #ошибка сертификата
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument("--window-size=1080,720")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

git_window_one = ("xpath", "//span[text() ='GitHub']")
favorit_window_two =("xpath","//a[text()='Вход и регистрация']")
login_window_three = ("xpath","//a[text()= 'Ozon Карта']")

# Шаг 1 - Открыть базовую страницу
driver.get("https://hyperskill.org/login")

# Шаг 2 - Получение дескриптора текущего окна
window_one = driver.current_window_handle
print("Дескриптор первого окна: ", window_one)
print(driver.title)

# Шаг 3 - Открытие и переключение на новое вкладке
driver.switch_to.new_window("tab")

# Шаг 4 - Получение дескриптора нового окна
driver.get("https://www.avito.ru/")
window_two = driver.current_window_handle
print("Дескриптор второго окна: ", window_two)
print(driver.title)

# Шаг 5 - Проверка, что окно переключилось
# assert new_window == driver.current_window_handle, "Окно не переключилось"
# time.sleep(2)

# Шаг 6 - Открытие страницы в новой вкладке и получение дескриптора
driver.switch_to.new_window("tab")
driver.get("https://www.ozon.ru/")
window_three = driver.current_window_handle
print("Дескриптор третьего окна: ", window_three)
print(driver.title)

# Шаг 7 - Переключение на  окно 1
driver.switch_to.window(window_one)

wait.until(EC.element_to_be_clickable(git_window_one)).click()
#driver.find_element(*git_window_one).click()


# Шаг 8 - Переключение на  окно 2
driver.switch_to.window(window_two)
wait.until(EC.element_to_be_clickable(favorit_window_two)).click()
#driver.find_element(*favorit_window_two).click()

# Шаг 9- Переключение на  окно 3
driver.switch_to.window(window_three)
#wait.until(EC.visibility_of_element_located(login_window_three)).click()
time.sleep(5)
driver.find_element(*favorit_window_two).click()