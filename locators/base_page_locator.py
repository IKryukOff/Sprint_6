from selenium.webdriver.common.by import By


class BasePageLocator:
    body_block = (By.XPATH, './/body')
    yandex_logo = (By.XPATH, './/img[@alt="Yandex"]/parent::a')
    scooter_logo = (By.XPATH, './/img[@alt="Scooter"]/parent::a')
    header_order_button = (
        By.XPATH, './/div[starts-with(@class, "Header")]/button[text()="Заказать"]')
    header_status_button = (
        By.XPATH, './/div[starts-with(@class, "Header")]/button[text()="Статус заказа"]')
    cookie_accept_button = (By.XPATH, './/button[text()="да все привыкли"]')
