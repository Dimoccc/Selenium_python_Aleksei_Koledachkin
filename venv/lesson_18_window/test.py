from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--window-size=1920,1080')
options.page_load_strategy = 'eager'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)
wait = WebDriverWait(driver, 15)


class HyperSkill:
    url = "https://hyperskill.org/"
    SIGN_IN_LOCATOR = ("xpath", "//div[text()='Sign in']")
    ASSERTION_HEADER = ("xpath", "//h2")

    def open_site(self) -> str:
        driver.get(self.url)
        return driver.current_window_handle


class WildBerries:
    url = "https://www.wildberries.ru/"
    SIGN_IN_LOCATOR = ("xpath", "(//a[@data-wba-header-name='Login'])[1]")
    ASSERTION_HEADER = ("xpath", "(//h2)[1]")

    def open_site(self) -> str:
        driver.get(self.url)
        return driver.current_window_handle


class Avito:
    url = "https://www.avito.ru/"
    SIGN_IN_LOCATOR = ("xpath", "//a[@data-marker='header/login-button']")
    ASSERTION_HEADER = ("xpath", "//form[@data-marker='login-form']/h2")

    def open_site(self) -> str:
        driver.get(self.url)
        return driver.current_window_handle


# Открываем все вкладки и сохраняем их дескрипторы
hs_window = HyperSkill().open_site()
driver.switch_to.new_window('tab')
wb_window = WildBerries().open_site()
driver.switch_to.new_window('tab')
avito_window = Avito().open_site()


# Переключаемся по вкладкам и выводим в консоль их заголовки
driver.switch_to.window(hs_window)
print(f'Title of hyperskill: {driver.title}')
driver.switch_to.window(wb_window)
print(f'Title of wildberries: {driver.title}')
driver.switch_to.window(avito_window)
print(f'Title of avito: {driver.title}')


# Переключаемся по вкладкам, выполняя клик по кнопке логина и подтверждая переход
# HyperSkill
driver.switch_to.window(hs_window)
wait.until(EC.element_to_be_clickable(HyperSkill.SIGN_IN_LOCATOR)).click()
assert 'Sign in to Hyperskill' in wait.until(EC.visibility_of_element_located(HyperSkill.ASSERTION_HEADER)).text

# WildBerries
driver.switch_to.window(wb_window)
wait.until(EC.element_to_be_clickable(WildBerries.SIGN_IN_LOCATOR)).click()
assert 'Войти или создать профиль' in wait.until(EC.visibility_of_element_located(WildBerries.ASSERTION_HEADER)).text

# Avito
driver.switch_to.window(avito_window)
wait.until(EC.element_to_be_clickable(Avito.SIGN_IN_LOCATOR)).click()
assert 'Вход' in wait.until(EC.visibility_of_element_located(Avito.ASSERTION_HEADER)).text
