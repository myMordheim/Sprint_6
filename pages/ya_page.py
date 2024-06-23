from locators.ya_locators import *
from pages.base_page import BasePage


class YaPage(BasePage):

    def ya_page_check_title(self):
        self.title_window_change_wait(dzen)
