import allure
from locators.base_page_locator import BasePageLocator
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(BasePageLocator):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        return (WebDriverWait(self.driver, timeout)
                .until(EC.presence_of_element_located(locator)))

    def find_elements(self, locator: tuple[str, str], timeout: int = 10) -> list[WebElement]:
        return (WebDriverWait(self.driver, timeout)
                .until(EC.presence_of_all_elements_located(locator)))

    @allure.step('Открываем страницу {url}')
    def driver_get_url(self, url: str) -> None:
        self.driver.get(url)

    @allure.step('Узнать текущую страницу')
    def current_url(self) -> str:
        return self.driver.current_url

    @allure.step('Подтвердить cookie')
    def click_accept_cookie(self) -> None:
        self.find_element(self.cookie_accept_button).click()

    @allure.step('Нажать на логотип "Яндекс"')
    def click_yandex_logo(self) -> None:
        self.find_element(self.yandex_logo).click()

    @allure.step('Нажать на логотип "Самокат"')
    def click_scooter_logo(self) -> None:
        self.find_element(self.scooter_logo).click()

    @allure.step('Перейти на последнюю вкладку')
    def switch_to_last_tab(self) -> None:
        self.driver.switch_to.window(self.driver.window_handles[-1])
