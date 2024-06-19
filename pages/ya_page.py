from selenium.webdriver.common.by import By
import allure
from helpers import FaqAnswers
from pages.base_page import BasePage

class YaPage(BasePage):
    dzen = 'Дзен'

    def ya_page_check_title(self):
        self.title_window_change_wait(self.dzen)
