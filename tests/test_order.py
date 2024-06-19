import allure
import time
import URLs
from conftest import *
from pages.scooter_main_page import ScooterMainPage
from pages.order_page import OrderPage
from URLs import *
class TestOrder:

    @allure.title("Позитивный пользовательский путь заказа самоката")
    @allure.description('Проверка функциональности всех инпутов, дропдаунов меню, при позитивном пользовательском пути')
    @pytest.mark.parametrize('metro, date, delivery_date, color, name, surname, adress, number, comment', OrderPage.data_for_parametrize_order_test)
    def test_click_faq_and_show_answer(self, driver, metro, date, delivery_date, color, name, surname, adress, number, comment):
        main_page = ScooterMainPage(driver)
        order_page = OrderPage(driver)
        main_page.change_url(base_url)
        main_page.click_cookies_button()
        main_page.click_order_button_middle()
        main_page.wait_for_element_visability(OrderPage.order_form_header_test)
        order_page.input_name(name)
        order_page.input_surname(surname)
        order_page.input_adress(adress)
        order_page.metro_dropdown_click()
        order_page.metro_choose(metro)
        order_page.number_input_method(number)
        order_page.button_next_click()
        order_page.dropdown_datepicker_click()
        order_page.date_choose(date)
        order_page.delivery_dropdown_click()
        order_page.delivery_date_choose(delivery_date)
        order_page.color_choose(color)
        order_page.input_comment(comment)
        order_page.click_an_order_button()
        order_page.confrim_order()
        assert 'Заказ оформлен' in order_page.text_order_confirmed()
