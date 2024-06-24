import allure

from pages.base_page import BasePage
from locators.locators import AuthPageLocators


class LoginPage(BasePage):

    @allure.step('Sending keys to "Email" field')  # Отправляем почту в поле ввода
    def send_keys_to_email_field(self, email):
        self.send_keys_into_field(AuthPageLocators.email_input_field, email)

    @allure.step('Sending keys to "Password" field')  # Отправляем пароль в поле ввода
    def send_keys_to_password_field(self, password):
        self.send_keys_into_field(AuthPageLocators.password_input_field, password)

    @allure.step('Click on "Login" button')  # Клик по кнопке "Логин" окна авторизации
    def click_on_login_button(self):
        self.click_on_button(AuthPageLocators.login_account_button)

    @allure.step('Authorization')  # Авторизуем созданного пользователя
    def authorization(self, email, password):
        self.send_keys_to_email_field(email)
        self.send_keys_to_password_field(password)
        self.click_on_login_button()

    @allure.step('Click on "Recovery" button')  # Клик по кнопке "Восстановить пароль" окна авторизации
    def click_on_recovery_button(self):
        self.click_on_button(AuthPageLocators.recovery_button)

    @allure.step("Check for login form")  # Проверяем наличие формы окна авторизации
    def check_presence_of_auth_form(self):
        return self.check_element(AuthPageLocators.authorization_form)
