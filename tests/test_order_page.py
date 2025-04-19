from time import sleep

import allure
import pytest
from data.order_page_input import OrderData, Orders
from data.urls import Urls
from locators.order_status_page_locator import OrderStatusPageLocator
from pages.order_page import OrderPage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.parent_suite('Тестирование сервиса заказа самоката')
@allure.suite('Тестирование страницы оформления заказа')
class TestOrderPage:
    @allure.sub_suite('Тестирование оформления заказа при вводе некорректных данных')
    @allure.title('Проверка некорректного ввода обязательного поля "Имя" значением: "{first_name}"')
    @allure.description('Заполняем поле Имени формы оформления заказа некорректным значением '
                        ' и проверяем вывод сообщения "Введите корректное имя"')
    @pytest.mark.parametrize('first_name', ['', 'И', 'Иvаn'])
    def test_fillup_incorrect_first_name_show_incorrect_message(self, driver: WebDriver,
                                                                first_name: str) -> None:
        order_page = OrderPage(driver)
        order_page.fillup_first_name(first_name)
        order_page.open_second_order_stage_form()

        assert order_page.find_element(order_page.incorrect_first_name_div).is_displayed()

    @allure.sub_suite('Тестирование оформления заказа при вводе некорректных данных')
    @allure.title('Проверка некорректного ввода обязательного поля "Фамилия"'
                  ' значением: "{last_name}"')
    @allure.description('Заполняем поле Фамилии формы оформления заказа некорректным значением '
                        'и проверяем вывод сообщения "Введите корректную фамилию"')
    @pytest.mark.parametrize('last_name', ['', 'И', 'Иvанов'])
    def test_fillup_incorrect_last_name_show_incorrect_message(self, driver: WebDriver,
                                                               last_name: str) -> None:
        order_page = OrderPage(driver)
        order_page.fillup_last_name(last_name)
        order_page.open_second_order_stage_form()

        assert order_page.find_element(order_page.incorrect_last_name_div).is_displayed()

    @allure.sub_suite('Тестирование оформления заказа при вводе некорректных данных')
    @allure.title('Проверка некорректного ввода обязательного поля "Адрес" значением: "{address}"')
    @allure.description('Заполняем поле Адреса формы оформления заказа некорректным значением '
                        'и проверяем вывод сообщения "Введите корректный адрес"')
    @pytest.mark.parametrize('address', ['', 'Вок', 'Вокзаl'])
    def test_fillup_incorrect_address_show_incorrect_message(self, driver: WebDriver,
                                                             address: str) -> None:
        order_page = OrderPage(driver)
        order_page.fillup_address(address)
        order_page.open_second_order_stage_form()

        assert order_page.find_element(order_page.incorrect_address_div).is_displayed()

    @allure.sub_suite('Тестирование оформления заказа при вводе некорректных данных')
    @allure.title('Проверка некорректного ввода обязательного поля "Станция метро')
    @allure.description('Никак не заполняем поле Станции метро и проверяем вывод сообщения '
                        '"Выберите станцию"')
    def test_fillup_incorrect_subway_station_show_incorrect_message(self,
                                                                    driver: WebDriver) -> None:
        order_page = OrderPage(driver)
        order_page.open_second_order_stage_form()

        assert order_page.find_element(order_page.incorrect_subway_div).is_displayed()

    @allure.sub_suite('Тестирование оформления заказа при вводе некорректных данных')
    @allure.title('Проверка некорректного ввода обязательного поля "Телефон" значением: '
                  '"{phone_number}"')
    @allure.description('Заполняем поле Телефона формы оформления заказа некорректным значением '
                        'и проверяем вывод сообщения "Введите корректный номер"')
    @pytest.mark.parametrize('phone_number', ['', '123456', '12345678901234'])
    def test_fillup_incorrect_phone_number_show_incorrect_message(self, driver: WebDriver,
                                                                  phone_number: str) -> None:
        order_page = OrderPage(driver)
        order_page.fillup_phome_number(phone_number)
        order_page.open_second_order_stage_form()

        assert order_page.find_element(order_page.incorrect_phone_number_div).is_displayed()

    @allure.sub_suite('Тестирование оформления заказа')
    @allure.title('Проверка оформления заказа и получении информации о заказе')
    @allure.description('Заполняем форму оформления заказа, подверждаем заказ и проверяем '
                        'получение информации о созданном заказе')
    @pytest.mark.parametrize('order_data', [Orders.inputs[0]])
    def test_order_fillup_form_show_order_text_info(self, driver: WebDriver,
                                                    order_data: OrderData) -> None:
        order_page = OrderPage(driver=driver)
        order_page.fillup_first_stage_order_form(order_data)
        order_page.open_second_order_stage_form()
        order_page.fillup_second_stage_order_form(order_data)
        order_page.click_finish_order()
        order_page.click_confirm_ordering()

        assert driver.find_element(*order_page.ordered_text_info) is not None

    @allure.sub_suite('Тестирование оформления заказа')
    @allure.title('Проверка оформления заказа и переход на страницу отслеживания '
                  'оформленного заказа')
    @allure.description('Заполняем форму оформления заказа, подверждаем заказ, получаем '
                        'информацию о созданном заказе и проверяем переход на страницу '
                        'отслеживания оформленного заказа')
    @pytest.mark.parametrize('order_data', [Orders.inputs[1]])
    def test_order_fillup_form_show_order_tracking_info(self, driver: WebDriver,
                                                        order_data: OrderData) -> None:
        order_page = OrderPage(driver=driver)
        order_page.fillup_first_stage_order_form(order_data)
        order_page.open_second_order_stage_form()
        order_page.fillup_second_stage_order_form(order_data)
        order_page.click_finish_order()
        order_page.click_confirm_ordering()
        order_page.click_show_tracking_info()

        assert (Urls.order_status_page in order_page.current_url()
                and order_page.find_element(OrderStatusPageLocator.order_status_roadmap))

    @allure.sub_suite('Тестирование шапки страницы')
    @allure.title('Проверка перехода на основную страницу при клике на логотип Самоката')
    @allure.description('На шапке страницы нажимамем на логотип "Самокат" и проверяем переход на '
                        'основную страницу')
    def test_click_scooter_logo_open_home_page(self, driver: WebDriver) -> None:
        order_page = OrderPage(driver=driver)
        order_page.click_scooter_logo()

        assert order_page.current_url() == Urls.home_page

    @allure.sub_suite('Тестирование шапки страницы')
    @allure.title('Проверка перехода на Дзен в новой вкладке при клике на логотип Яндекса')
    @allure.description('На шапке страницы нажимамем на логотип "Яндекс" и проверяем открытие '
                        'страницы Дзена на новой вкладке')
    def test_click_yandex_logo_open_dzen_page(self, driver: WebDriver) -> None:
        order_page = OrderPage(driver=driver)
        order_page.click_yandex_logo()
        order_page.switch_to_last_tab()
        sleep(3)

        assert Urls.dzen_page in order_page.current_url()
