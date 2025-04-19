import allure
from time import sleep

from data.urls import Urls
from pages.order_status_page import OrderStatusPage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.parent_suite('Тестирование сервиса заказа самоката')
@allure.suite('Тестирование страницы отслеживания заказа')
class TestHomePage:
    @allure.sub_suite('Тестирование шапки страницы')
    @allure.title('Проверка перехода на основную страницу при клике на логотип Самоката')
    @allure.description('На шапке страницы нажимамем на логотип "Самокат" и проверяем переход на '
                        'основную страницу')
    def test_click_scooter_logo_open_home_page(self, driver: WebDriver) -> None:
        order_status_page = OrderStatusPage(driver=driver)
        order_status_page.click_scooter_logo()

        assert order_status_page.current_url() == Urls.home_page

    @allure.sub_suite('Тестирование шапки страницы')
    @allure.title('Проверка перехода на Дзен в новой вкладке при клике на логотип Яндекса')
    @allure.description('На шапке страницы нажимамем на логотип "Яндекс" и проверяем открытие '
                        'страницы Дзена на новой вкладке')
    def test_click_yandex_logo_open_dzen_page(self, driver: WebDriver) -> None:
        order_status_page = OrderStatusPage(driver=driver)
        order_status_page.click_yandex_logo()
        order_status_page.switch_to_last_tab()
        sleep(3)

        assert Urls.dzen_page in order_status_page.current_url()
