import allure
import URLs
from conftest import *
from pages.scooter_main_page import ScooterMainPage
from pages.order_page import OrderPage
from pages.ya_page import YaPage
from URLs import *


class TestMainPage:

    @allure.title('Проверка открытия в новой вкладке Дзен')
    @allure.description("Клик по логотипу Дзен и редирект")
    def test_yandex_header_redirect(self, driver):
        main_page = ScooterMainPage(driver)
        ya_page = YaPage(driver)
        main_page.change_url(base_url)
        main_page.click_ya_logo()
        main_page.switch_to_window()
        ya_page.ya_page_check_title()
        assert main_page.get_current_url() == URLs.ya_dzen_url

    @allure.title('Проверка перехода по логотипу Самокат')
    @allure.description("Клик по логотипу Самокат")
    def test_scooter_header_redirect(self, driver):
        main_page = ScooterMainPage(driver)
        order_page = OrderPage(driver)
        order_page.change_url(order_url)
        order_page.click_samokat_logo()
        assert main_page.get_current_url() == URLs.base_url
    @allure.title('Проверка функциональности перехода в заказ через кнопку "Заказать"')
    @allure.description("Клик по кнопке 'Заказать' в середине страницы")
    def test_click_order_button_header(self, driver):
        main_page = ScooterMainPage(driver)
        main_page.change_url(base_url)
        main_page.click_cookies_button()
        main_page.click_order_button_middle()
        main_page.wait_for_element_visability(OrderPage.order_form_header_test)
        assert main_page.get_current_url() == URLs.order_url

    @allure.title('Проверка функциональности перехода в заказ через кнопку "Заказать"')
    @allure.description("Клик по кнопке 'Заказать' в хеддере страницы")
    def test_click_order_button_header(self, driver):
        main_page = ScooterMainPage(driver)
        main_page.change_url(base_url)
        main_page.click_cookies_button()
        main_page.click_order_button()
        main_page.wait_for_element_visability(OrderPage.order_form_header_test)
        assert main_page.get_current_url() == URLs.order_url

    @allure.title("Проверка функционала FAQ")
    @allure.description('Клик на элемент FAQ и отображение элемента "Ответ"')
    @pytest.mark.parametrize('faq, faq_answer, assert_faq_answer', ScooterMainPage.faq_data_parametrize)
    def test_click_faq_and_show_answer(self, driver, faq, faq_answer, assert_faq_answer):
        main_page = ScooterMainPage(driver)
        main_page.change_url(base_url)
        main_page.click_cookies_button()
        main_page.click_faq(faq)
        main_page.wait_for_element_visability(faq_answer)
        assert main_page.find_answer_faq(faq_answer) == assert_faq_answer
