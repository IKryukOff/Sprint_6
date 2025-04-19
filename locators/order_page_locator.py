from locators.base_page_locator import BasePageLocator
from selenium.webdriver.common.by import By


class OrderPageLocator(BasePageLocator):
    # First stage order form elements
    first_name_input = (By.XPATH, './/input[@placeholder="* Имя"]')
    last_name_input = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    address_input = (By.XPATH, './/input[contains(@placeholder, "Адрес")]')
    subway_station_field = (By.XPATH, './/input[contains(@placeholder, "метро")]')
    phone_number_input = (By.XPATH, './/input[contains(@placeholder, "Телефон")]')
    # First stage order form elements incorrect elements
    incorrect_first_name_div = (
        By.XPATH, './/input[@placeholder="* Имя"]/parent::div/div')
    incorrect_last_name_div = (
        By.XPATH, './/input[@placeholder="* Фамилия"]/parent::div/div')
    incorrect_address_div = (
        By.XPATH, './/input[contains(@placeholder, "Адрес")]/parent::div/div')
    incorrect_subway_div = (
        By.XPATH,
        './/input[contains(@placeholder, "метро")]/parent::*/parent::*/parent::div/div[contains(@class, "Error")]')
    incorrect_phone_number_div = (
        By.XPATH, './/input[contains(@placeholder, "Телефон")]/parent::div/div')

    next_button = (By.XPATH, './/button[text()="Далее"]')
    # Second stage order form elements
    date_input = (By.XPATH, './/input[contains(@placeholder, "Когда")]')
    order_duration_field = (By.CLASS_NAME, 'Dropdown-arrow')
    order_duration_list = (By.CLASS_NAME, 'Dropdown-option')
    notes_input = (By.XPATH, './/input[contains(@placeholder, "Комментарий для курьера")]')

    order_button = (By.XPATH, './/div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    confirm_order_text = (By.XPATH, './/div[text()="Хотите оформить заказ?"]')
    confirm_order_yes_button = (By.XPATH, './/button[text()="Да"]')
    ordered_text_info = (By.XPATH, './/div[contains(text(), "Номер заказа")]')
    track_order_button = (By.XPATH, './/button[text()="Посмотреть статус"]')

    @staticmethod
    def subway_station_button(name: str) -> tuple[str, str]:
        return (By.XPATH, f'.//div[text()="{name}"]/parent::button')

    @staticmethod
    def color_label(color: str) -> tuple[str, str]:
        return (By.XPATH, f'.//div[contains(text(),"Цвет")]/parent::*/label[@for="{color}"]')
