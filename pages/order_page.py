import allure
from pages.base_page import BasePage
from locators.order_locators import *


class OrderPage(BasePage):

    @allure.step('Заполнить инпут Имя')
    def input_name(self, name):
        self.send_text(name_input, name)

    @allure.step('Заполнить инпут Фамилия')
    def input_surname(self, surname):
        self.send_text(surname_input, surname)

    @allure.step('Заполнить инпут Адресс')
    def input_adress(self, adress):
        self.send_text(adress_input, adress)

    @allure.step('Раскрыть дропдаун метро')
    def metro_dropdown_click(self):
        self.click_element(metro_input)

    @allure.step('Выбрать метро')
    def metro_choose(self, metro):
        self.click_element(metro)

    @allure.step('Заполнить инпут Номер телефона')
    def number_input_method(self, number):
        self.send_text(number_input, number)

    @allure.step('Нажать на кнопку Далее')
    def button_next_click(self):
        self.click_element(button_next)

    @allure.step('Раскрыть календарь')
    def dropdown_datepicker_click(self):
        self.click_element(datepicker_input)

    @allure.step('Выбрать дату')
    def date_choose(self, date):
        self.click_element(date)

    @allure.step('Раскрыть дропдаун срок доставки')
    def delivery_dropdown_click(self):
        self.click_element(rent)

    @allure.step('Выбрать срок доставки')
    def delivery_date_choose(self, delivery_date):
        self.click_element(delivery_date)

    @allure.step('Выбрать цвет')
    def color_choose(self, color):
        self.click_element(color)

    @allure.step('Заполнить инпут Комментарий для курьера')
    def input_comment(self, comment):
        self.send_text(comment_for_courier, comment)

    @allure.step('Кликнуть на кнопку Заказать')
    def click_an_order_button(self):
        self.click_element(make_an_order_button)

    @allure.step('Кликнуть на кнопку Да')
    def confrim_order(self):
        self.click_element(confirm_an_order_button)

    @allure.step('Получить элемент: "Заказ оформлен"')
    def text_order_confirmed(self):
        return self.find_text_element(for_assert)

    @allure.step('Получить элемент модального окна: "Заказ оформлен"')
    def order_confirmed(self):
        return self.find_element(for_assert)

    @allure.step('Клик на лого Самокат')
    def click_samokat_logo(self):
        self.click_element(samokat_header)
