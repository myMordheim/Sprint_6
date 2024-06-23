from selenium.webdriver.common.by import By
from helpers import FaqAnswers

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
