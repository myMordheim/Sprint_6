import allure
import pytest
from conftest import *
from pages.scooter_main_page import ScooterMainPage
from URLs import *


class TestMainPage:

    @allure.title("Проверка функционала FAQ")
    @allure.description('Клик на элемент FAQ и отображение элемента "Ответ"')
    @pytest.mark.parametrize('faq, faq_answer, assert_faq_answer', ScooterMainPage.faq_data_parametrize)
    def test_click_faq_and_show_answer(self, driver, faq, faq_answer, assert_faq_answer):
        driver.get(base_url)
        ScooterMainPage.click_faq(faq)
        assert ScooterMainPage.find_answer_faq(faq_answer) == assert_faq_answer
