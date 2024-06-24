import allure
from pages.base_page import BasePage
from locators.scooter_locators import *


class ScooterMainPage(BasePage):

    @allure.step('Клик по кнопке "да все привыкли"')
    def click_cookies_button(self):
        self.click_element(cookies_button)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self.click_element(order_button)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button_middle(self):
        self.click_element(middle_order_button)

    @allure.step('Клик на лого Яндекс Дзен')
    def click_ya_logo(self):
        self.click_element(yandex_dzen_header)

    @allure.step('Скролл к FAQ')
    def scroll_to_faq(self, faq):
        self.scroll_to_element(faq)

    @allure.step('Нажать и раскрыть FAQ')
    def click_faq(self, faq):
        self.click_element(faq)

    @allure.step('Найти ответ на FAQ')
    def find_answer_faq(self, faq_answer):
        return self.find_text_element(faq_answer)
