from data.urls import Urls
from locators.order_status_page_locator import OrderStatusPageLocator
from pages.base_page import BasePage
from selenium.webdriver.firefox.webdriver import WebDriver


class OrderStatusPage(BasePage, OrderStatusPageLocator):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver_get_url(Urls.order_page)
        self.click_accept_cookie()
