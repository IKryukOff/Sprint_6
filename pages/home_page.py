import allure
from data.urls import Urls
from locators.home_page_locator import HomePageLocator
from pages.base_page import BasePage
from selenium.webdriver.firefox.webdriver import WebDriver


class HomePage(BasePage, HomePageLocator):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver_get_url(Urls.home_page)
        self.click_accept_cookie()

    @allure.step('Нажать на {question_number}-й вопрос')
    def click_faq_question(self, question_number: int) -> None:
        self.find_elements(self.faq_questions)[question_number - 1].click()

    @allure.step('Нажать на кнопку "Заказать" в шапке страницы')
    def click_header_order_button(self) -> None:
        self.find_element(self.header_order_button).click()

    @allure.step('Нажать на кнопку "Заказать" на основной странице')
    def click_home_order_button(self) -> None:
        self.find_element(self.home_order_button).click()
