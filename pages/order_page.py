import allure
from data.order_page_input import OrderData
from data.urls import Urls
from locators.order_page_locator import OrderPageLocator
from pages.base_page import BasePage
from selenium.webdriver.firefox.webdriver import WebDriver


class OrderPage(BasePage, OrderPageLocator):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver_get_url(Urls.order_page)
        self.click_accept_cookie()

    @allure.step('Заполнить поле "Имя" формы оформления заказа')
    def fillup_first_name(self, first_name: str) -> None:
        self.find_element(self.first_name_input).send_keys(first_name)

    @allure.step('Заполнить поле "Фамилия" формы оформления заказа')
    def fillup_last_name(self, last_name: str) -> None:
        self.find_element(self.last_name_input).send_keys(last_name)

    @allure.step('Заполнить поле "Адрес" формы оформления заказа')
    def fillup_address(self, address: str) -> None:
        self.find_element(self.address_input).send_keys(address)

    @allure.step('Заполнить поле "Станция метро" формы оформления заказа')
    def choose_subway_station(self, name: str) -> None:
        self.find_element(self.subway_station_field).click()
        self.find_element(self.subway_station_button(name)).click()

    @allure.step('Заполнить поле "Телефон" формы оформления заказа')
    def fillup_phome_number(self, phone_number: str) -> None:
        self.find_element(self.phone_number_input).send_keys(phone_number)

    @allure.step('Нажать на кнопке "Далее" формы оформления заказа')
    def open_second_order_stage_form(self) -> None:
        self.find_element(self.next_button).click()

    @allure.step('Заполнить поле "Когда привезти самокат" формы оформления заказа')
    def fiilup_date(self, date) -> None:
        self.find_element(self.date_input).send_keys(date)

    @allure.step('Заполнить поле "Срок аренды" формы оформления заказа')
    def choose_order_duration(self, order_duration: int) -> None:
        self.find_element(self.order_duration_field).click()
        self.find_elements(self.order_duration_list)[order_duration - 1].click()

    @allure.step('Заполнить поле "Цвет самоката" формы оформления заказа')
    def choose_color(self, color: str) -> None:
        self.find_element(self.color_label(color)).click()

    @allure.step('Заполнить поле "Комментарий для курьера" формы оформления заказа')
    def fillup_notes(self, notes: str) -> None:
        self.find_element(self.notes_input).send_keys(notes)

    @allure.step('Нажать на кнопку "Заказать" формы оформления заказа')
    def click_finish_order(self) -> None:
        self.find_element(self.order_button).click()

    @allure.step('Нажать на кнопку "Да" для подтверждения заказа')
    def click_confirm_ordering(self) -> None:
        self.find_element(self.confirm_order_yes_button).click()

    @allure.step('Нажать на кнопку "Посмотреть статус" после подтверждения заказа')
    def click_show_tracking_info(self) -> None:
        self.find_element(self.track_order_button).click()

    @allure.step('Заполнить 1-ю часть формы оформления заказа')
    def fillup_first_stage_order_form(self, order_data: OrderData) -> None:
        self.fillup_first_name(order_data.first_name)
        self.fillup_last_name(order_data.last_name)
        self.fillup_address(order_data.address)
        self.choose_subway_station(order_data.subway_station)
        self.fillup_phome_number(order_data.phone_number)

    @allure.step('Заполнить 2-ю часть формы оформления заказа')
    def fillup_second_stage_order_form(self, order_data: OrderData) -> None:
        self.fiilup_date(order_data.date)
        self.choose_order_duration(order_data.order_duration)
        for color in order_data.color:
            self.choose_color(color)
        self.fillup_notes(order_data.notes)
