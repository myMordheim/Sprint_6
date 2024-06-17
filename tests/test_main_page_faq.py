import allure
from conftest import *
from pages.scooter_main_page import ScooterMainPage
from URLs import *


class TestMainPage:

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
