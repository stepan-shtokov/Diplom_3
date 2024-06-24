import allure

from pages.base_page import BasePage
from locators.locators import MainPageLocators
from locators.locators import HeaderLocators


class HeaderMainPage(BasePage):

    @allure.step("Click on 'Constructor' button")  # Клик по кнопке "Конструктор" хедера главной страницы
    def click_on_construction_button_in_header(self):
        self.click_on_button(HeaderLocators.constructor_button)

    @allure.step('Click on "Order feed" button')  # Клик по кнопке "Лента заказов" хедера главной страницы
    def click_on_order_feed_button_in_header(self):
        self.click_on_button(HeaderLocators.order_feed_button)

    @allure.step('Click on "PersonalProfile" button')  # Клик по кнопке "Личный Кабинет" хедера главной страницы
    def click_on_personal_profile_button_in_header(self):
        self.click_on_button(HeaderLocators.personal_account_button)


class MainPage(BasePage):

    @allure.step('Check for constructor form being visible')  # Проверка отображения формы конструктора главной страницы
    def check_constructor_form(self):
        return self.check_element(MainPageLocators.constructor_form)

    @allure.step('Check for order feed form being visible')  # Проверяем отображение ленты заказов
    def check_order_feed_form(self):
        return self.check_element(MainPageLocators.feed_order_form)

    @allure.step('Click on "PersonalAccount" button')  # Клик по кнопке "Войти в аккаунт" на главной странице
    def click_on_personal_account_button_mainpage(self):
        self.click_on_button(MainPageLocators.personal_account_login_button)

    @allure.step('Click on fluorescent bun in constructor')  # Клик по флуоресцентной булочке в конструкторе
    def click_on_bun_in_constructor(self):
        self.click_on_button(MainPageLocators.fluorescent_bun_button)

    @allure.step('Check for informational ingredient popup being displayed')  # Проверяем отображение модального окна ингредиента
    def check_bun_info_displayed(self):
        return self.check_element(MainPageLocators.popup_from_ingredient)

    @allure.step('Close informational popup')  # Закрыть модальное окно ингредиента кликом по крестику
    def close_info_popup(self):
        self.click_on_button(MainPageLocators.closing_cross_button)

    @allure.step('Check for info popup is closed')  # Проверяем, что модальное окно не отображается\закрыто
    def check_close_bun_info(self):
        return self.check_is_element_not_visible(MainPageLocators.popup_from_ingredient)

    @allure.step("Check for PlaceOrder button being loaded")  # Проверяем, что кнопка "Оформить заказ" отображается
    def wait_place_order_button_visible(self):
        self.wait_loading_element(MainPageLocators.order_place_button)

    @allure.step('Check of order form being displayed')  # Проверяем отображение формы заказа главной страницы
    def check_order_form_being_displayed(self):
        return self.check_element(MainPageLocators.order_form)

    @allure.step('Add bun to order basket')  # Добавляем булочку в корзину заказа
    def bun_add_to_basket(self):
        self.drag_drop(MainPageLocators.fluorescent_bun_button, MainPageLocators.order_basket)

    @allure.step('Click on "PlaceOrder" button')  # Клик по кнопке "Оформить заказ"
    def click_on_place_order_button(self):
        self.click_on_button(MainPageLocators.order_place_button)

    @allure.step('Get number of ingredients')  # Получаем счетчик кол-ва ингредиентов  в заказе
    def get_number_of_ingredients_in_order(self):
        self.wait_loading_element(MainPageLocators.ingredient_counter)
        return self.get_text_from_locator(MainPageLocators.ingredient_counter)

    @allure.step('Create an order')
    def create_an_order(self):  # Оформляем заказ
        self.bun_add_to_basket()
        self.click_on_place_order_button()
