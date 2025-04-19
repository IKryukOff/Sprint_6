from time import sleep

import allure
import pytest
from data.home_page_faq import FAQ
from data.urls import Urls
from pages.home_page import HomePage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.parent_suite('Тестирование сервиса заказа самоката')
@allure.suite('Тестирование основной страницы')
class TestHomePage:
    @allure.sub_suite('Тестирование FAQ')
    @allure.title('Проверка корректности вопрос-ответ для вопроса №{question_number}')
    @allure.description('На странице нажимаем на вопрос и проверям что получаем ожидаемый ответ')
    @pytest.mark.parametrize('question_number,expected_answer', FAQ.answers)
    def test_faq_click_question_show_answer(self, driver: WebDriver,
                                            question_number: int,
                                            expected_answer: str) -> None:
        home_page = HomePage(driver=driver)
        home_page.click_faq_question(question_number=question_number)

        assert home_page.find_element(home_page.faq_answer).text == expected_answer

    @allure.sub_suite('Тестирование перехода на страницу оформления заказа')
    @allure.title('Проверка перехода на страницу оформления заказа через кнопку в шапке страницы')
    @allure.description('На шапке страницы нажимаем на кнопку "Заказать" и проверяем переход на '
                        'страницу оформления заказа')
    def test_click_header_order_button_open_order_page(self, driver: WebDriver) -> None:
        home_page = HomePage(driver=driver)
        home_page.click_header_order_button()

        assert home_page.current_url() == Urls.order_page

    @allure.sub_suite('Тестирование перехода на страницу оформления заказа')
    @allure.title('Проверка перехода на страницу оформления заказа через кнопку в центре страницы')
    @allure.description('В центре страницы нажимаем на кнопку "Заказать" и проверяем переход на '
                        'страницу оформления заказа')
    def test_click_home_order_button_open_order_page(self, driver: WebDriver) -> None:
        home_page = HomePage(driver=driver)
        home_page.click_home_order_button()

        assert home_page.current_url() == Urls.order_page

    @allure.sub_suite('Тестирование шапки страницы')
    @allure.title('Проверка перехода на основную страницу при клике на логотип Самоката')
    @allure.description('На шапке страницы нажимамем на логотип "Самокат" и проверяем переход на '
                        'основную страницу')
    def test_click_scooter_logo_open_home_page(self, driver: WebDriver) -> None:
        home_page = HomePage(driver=driver)
        home_page.click_scooter_logo()

        assert home_page.current_url() == Urls.home_page

    @allure.sub_suite('Тестирование шапки страницы')
    @allure.title('Проверка перехода на Дзен в новой вкладке при клике на логотип Яндекса')
    @allure.description('На шапке страницы нажимамем на логотип "Яндекс" и проверяем открытие '
                        'страницы Дзена на новой вкладке')
    def test_click_yandex_logo_open_dzen_page(self, driver: WebDriver) -> None:
        home_page = HomePage(driver=driver)
        home_page.click_yandex_logo()
        home_page.switch_to_last_tab()
        sleep(3)

        assert Urls.dzen_page in home_page.current_url()
