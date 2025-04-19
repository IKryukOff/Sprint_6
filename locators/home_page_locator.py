from locators.base_page_locator import BasePageLocator
from selenium.webdriver.common.by import By


class HomePageLocator(BasePageLocator):
    home_order_button = (
        By.XPATH, './/div[starts-with(@class, "Home")]/button[text()="Заказать"]')
    faq_questions = (By.XPATH, './/div[@class="accordion__button"]')
    faq_answer = (By.XPATH, './/div[@class="accordion__panel" and not(@hidden)]/p')
