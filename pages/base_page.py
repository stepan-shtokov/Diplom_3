from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):  # Получить текущий URL-адрес
        return self.driver.current_url

    def wait_loading_element(self, locator):  # Ожидание загрузки элемента
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def send_keys_into_field(self, locator, text):  # Отправить значение в поле
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def click_on_button(self, locator):  # Клик по элементу через скрипт
        element = self.wait_loading_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def check_element(self, locator):  # Проверить наличие элемента
        self.wait_loading_element(locator)
        return self.driver.find_element(*locator)

    def get_text(self, locator):  # Получить текст локаторов
        WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def drag_drop(self, element_first, element_second):  # Метод перетаскивания, аналог ActionChains(последний не работает в Firefox)
        ingredient = self.check_element(element_first)
        basket = self.check_element(element_second)
        drag_and_drop(self.driver, ingredient, basket)

    def check_is_element_not_visible(self, locator):  # Проверяем, что элемент не отображается
        WebDriverWait(self.driver, 5).until(ec.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_text_from_locator(self, locator):  # Получить текст элемента
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def click_after_wait(self, locator):  # Клик без скрипта с ожиданием отображения
        target_to_click = self.wait_loading_element(locator)
        target_to_click.click()
