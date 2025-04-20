from locators.base_page_locator import BasePageLocator
from selenium.webdriver.common.by import By


class OrderStatusPageLocator(BasePageLocator):
    order_status_roadmap = (By.XPATH, './/div[contains(@class, "Track_OrderRoadmap")]')
