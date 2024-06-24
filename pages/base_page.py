import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    @allure.step('Получить текущий адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переход')
    def change_url(self, url):
        self.driver.get(url)

    @allure.step('Ожидание оторбражения видимости элемента')
    def wait_for_visability(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание: переход на другой url')
    def wait_url_change(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(url))

    @allure.step('Найти элемент')
    def find_element(self, locator):
        self.driver.find_element(*locator)
        try:
            return WebDriverWait(self.driver).until(expected_conditions.presence_of_element_located(locator))
        except:
            print(f'"Элемент с локатором - "{locator} не найден')
            return None

    @allure.step('Найти элемент')
    def find_element_for_result(self, locator):
        return self.driver.find_element(locator)

    @allure.step('Кликнуть на элемент')
    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step('Подождать отображение элемента')
    def wait_for_element_visability(self, locator):
        WebDriverWait(self.driver, 5).until((expected_conditions.visibility_of_element_located(locator)))

    @allure.step('Найти текст')
    def find_text_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    @allure.step('Написать текст в инпут')
    def send_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    @allure.step('Проскроллить к элементу')
    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator))

    @allure.step('Перейты в новое открытое окно')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ожидание смены тайтла вкладки')
    def title_window_change_wait(self, title):
        WebDriverWait(self.driver, 5).until(expected_conditions.title_is(title))
