from selenium.webdriver.common.by import By
import allure
from helpers import OrderData
from pages.base_page import BasePage


class OrderPage(BasePage):
    order_form_header_test = (By.XPATH, './/div[text()="Для кого самокат"]')
    name_input = (By.XPATH, ".//input[@placeholder = '* Имя']")
    surname_input = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    adress_input = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro_input = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    metro_1 = (By.XPATH, ".//div[text() = 'Спортивная']")
    metro_2 = (By.XPATH, ".//div[text() = 'Парк культуры']")
    number_input = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, ".//button[text() = 'Далее']")
    datepicker_input = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    order_date_one = (By.XPATH, ".//div[@class = 'react-datepicker__day react-datepicker__day--013']")
    order_date_two = (By.XPATH, ".//div[@class = 'react-datepicker__day react-datepicker__day--003']")
    rent = (By.XPATH, ".//div[text() = '* Срок аренды']")
    three_days_grace = (By.XPATH, ".//div[text() = 'трое суток']")
    five_days_gone = (By.XPATH, ".//div[text() = 'пятеро суток']")
    color_black = (By.XPATH, ".//input[@id = 'black']")
    color_gray = (By.XPATH, ".//input[@id = 'grey']")
    comment_for_courier = (By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']")
    make_an_order_button = (By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    confirm_an_order_button = (By.XPATH, ".//button[text() = 'Да']")
    for_assert = (By.XPATH, './/div[@class="Order_ModalHeader__3FDaJ"]')
    samokat_header = (By.XPATH, './/a[2]/img')
    yandex_dzen_header = (By.XPATH, './/a[1]/img')

    data_for_parametrize_order_test = [[metro_1, order_date_one, three_days_grace, color_black, [OrderData.first_user[0]], [OrderData.first_user[1]], [OrderData.first_user[2]], [OrderData.first_user[3]], [OrderData.first_user[4]]],
                                       [metro_2, order_date_two, five_days_gone, color_gray, [OrderData.second_user[0]], [OrderData.second_user[1]], [OrderData.second_user[2]], [OrderData.second_user[3]], [OrderData.second_user[4]]]]
    @allure.step('Заполнить инпут Имя')
    def input_name(self, name):
        self.send_text(self.name_input, name)

    @allure.step('Заполнить инпут Фамилия')
    def input_surname(self, surname):
        self.send_text(self.surname_input, surname)

    @allure.step('Заполнить инпут Адресс')
    def input_adress(self, adress):
        self.send_text(self.adress_input, adress)

    @allure.step('Раскрыть дропдаун метро')
    def metro_dropdown_click(self):
        self.click_element(self.metro_input)

    @allure.step('Выбрать метро')
    def metro_choose(self, metro):
        self.click_element(metro)

    @allure.step('Заполнить инпут Номер телефона')
    def number_input_method(self, number):
        self.send_text(self.number_input, number)

    @allure.step('Нажать на кнопку Далее')
    def button_next_click(self):
        self.click_element(self.button_next)

    @allure.step('Раскрыть календарь')
    def dropdown_datepicker_click(self):
        self.click_element(self.datepicker_input)

    @allure.step('Выбрать дату')
    def date_choose(self, date):
        self.click_element(date)

    @allure.step('Раскрыть дропдаун срок доставки')
    def delivery_dropdown_click(self):
        self.click_element(self.rent)

    @allure.step('Выбрать срок доставки')
    def delivery_date_choose(self, delivery_date):
        self.click_element(delivery_date)

    @allure.step('Выбрать цвет')
    def color_choose(self, color):
        self.click_element(color)

    @allure.step('Заполнить инпут Комментарий для курьера')
    def input_comment(self, comment):
        self.send_text(self.comment_for_courier, comment)

    @allure.step('Кликнуть на кнопку Заказать')
    def click_an_order_button(self):
        self.click_element(self.make_an_order_button)

    @allure.step('Кликнуть на кнопку Да')
    def confrim_order(self):
        self.click_element(self.confirm_an_order_button)

    @allure.step('Получить элемент: "Заказ оформлен"')
    def text_order_confirmed(self):
        return self.find_text_element(self.for_assert)

    @allure.step('Клик на лого Самокат')
    def click_samokat_logo(self):
        self.click_element(self.samokat_header)