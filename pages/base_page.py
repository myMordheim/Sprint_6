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

    @allure.step('Ожидание: переход на другой url')
    def wait_url_change(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(url))

    @allure.step('Найти элемент')
    def find_element(self, locator):
        self.driver.find_element(locator)

    @allure.step('Кликнуть на элемент')
    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step('Подождать отображение элемента')
    def wait_for_element_visability(self, locator):
        WebDriverWait(self.driver, 5).until((expected_conditions.visibility_of_element_located(locator)))

    @allure.step('Найти текст')
    def find_text_element(self, locator):
        text = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text
        return text

    @allure.step('Проскроллить к элементу')
    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator))
