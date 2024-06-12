import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    @allure.step('Получить текущий адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание: переход на другой url')
    def wait_url_change(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(url))

    @allure.step('Найти элемент')
    def find_element(self, locator=tuple):
        self.driver.find_element(locator)
        try:
            return WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(locator))
        except:
            print(f'Элемент {locator} не был найден')

    @allure.step('Кликнуть на элемент')
    def click_element(self, locator=tuple):
        element = self.find_element(locator)
        try:
            element.click()
        except:
            print(f'Невозможно кликнуть на элемент{locator}')

    @allure.step('Найти текст')
    def find_text_element(self, locator=tuple):
        try:
            return self.find_element(locator).text
        except:
            print(f'Невозможно отобразить текст по элементу{locator}')
