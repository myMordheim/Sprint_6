from selenium.webdriver.common.by import By
from helpers import OrderData

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

data_for_parametrize_order_test = [
    [metro_1, order_date_one, three_days_grace, color_black, [OrderData.first_user[0]], [OrderData.first_user[1]],
     [OrderData.first_user[2]], [OrderData.first_user[3]], [OrderData.first_user[4]]],
    [metro_2, order_date_two, five_days_gone, color_gray, [OrderData.second_user[0]], [OrderData.second_user[1]],
     [OrderData.second_user[2]], [OrderData.second_user[3]], [OrderData.second_user[4]]]]
