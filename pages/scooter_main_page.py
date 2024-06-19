from selenium.webdriver.common.by import By
import allure
from helpers import FaqAnswers
from pages.base_page import BasePage


class ScooterMainPage(BasePage):
    cookies_button = (By.XPATH, './/button[text()="да все привыкли"]')
    order_button = (By.XPATH, './/button[text()="Заказать"]')
    samokat_header = (By.XPATH, './/a[2]/img')
    yandex_dzen_header = (By.XPATH, './/a[1]/img')
    middle_order_button = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button')
    faq_0 = (By.XPATH, './/div[@id="accordion__heading-0"]')
    faq_1 = (By.XPATH, './/div[@id="accordion__heading-1"]')
    faq_2 = (By.XPATH, './/div[@id="accordion__heading-2"]')
    faq_3 = (By.XPATH, './/div[@id="accordion__heading-3"]')
    faq_4 = (By.XPATH, './/div[@id="accordion__heading-4"]')
    faq_5 = (By.XPATH, './/div[@id="accordion__heading-5"]')
    faq_6 = (By.XPATH, './/div[@id="accordion__heading-6"]')
    faq_7 = (By.XPATH, './/div[@id="accordion__heading-7"]')
    faq_answer_0 = (By.XPATH, './/div[@id="accordion__panel-0"]//p')
    faq_answer_1 = (By.XPATH, './/div[@id="accordion__panel-1"]//p')
    faq_answer_2 = (By.XPATH, './/div[@id="accordion__panel-2"]//p')
    faq_answer_3 = (By.XPATH, './/div[@id="accordion__panel-3"]//p')
    faq_answer_4 = (By.XPATH, './/div[@id="accordion__panel-4"]//p')
    faq_answer_5 = (By.XPATH, './/div[@id="accordion__panel-5"]//p')
    faq_answer_6 = (By.XPATH, './/div[@id="accordion__panel-6"]//p')
    faq_answer_7 = (By.XPATH, './/div[@id="accordion__panel-7"]//p')

    faq_data_parametrize = [[faq_0, faq_answer_0, FaqAnswers.answer[0]],
                            [faq_1, faq_answer_1, FaqAnswers.answer[1]],
                            [faq_2, faq_answer_2, FaqAnswers.answer[2]],
                            [faq_3, faq_answer_3, FaqAnswers.answer[3]],
                            [faq_4, faq_answer_4, FaqAnswers.answer[4]],
                            [faq_5, faq_answer_5, FaqAnswers.answer[5]],
                            [faq_6, faq_answer_6, FaqAnswers.answer[6]],
                            [faq_7, faq_answer_7, FaqAnswers.answer[7]]
                            ]



    @allure.step('Клик по кнопке "да все привыкли"')
    def click_cookies_button(self):
        self.click_element(self.cookies_button)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self.click_element(self.order_button)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button_middle(self):
        self.click_element(self.middle_order_button)

    @allure.step('Клик на лого Яндекс Дзен')
    def click_ya_logo(self):
        self.click_element(self.yandex_dzen_header)

    @allure.step('Скролл к FAQ')
    def scroll_to_faq(self, faq):
        self.scroll_to_element(faq)

    @allure.step('Нажать и раскрыть FAQ')
    def click_faq(self, faq):
        self.click_element(faq)

    @allure.step('Найти ответ на FAQ')
    def find_answer_faq(self, faq_answer):
        return self.find_text_element(faq_answer)
