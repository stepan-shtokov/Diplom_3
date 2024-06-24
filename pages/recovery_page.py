import allure

from pages.base_page import BasePage
from locators.locators import RecoverPageLocators


class RecoveryPage(BasePage):
    @allure.step('Check for password recovery form')
    def check_recovery_form(self):  # Проверка отображения формы восстановления
        return self.check_element(RecoverPageLocators.recover_form_text)

    @allure.step('Send keys to "Email" input form')
    def send_keys_to_email_field(self, email):  # Отправляем значение email в соответствующее поле
        self.send_keys_into_field(RecoverPageLocators.email_input_field, email)

    @allure.step('Send keys to "Password" input form')
    def send_keys_to_password_field(self, password):  # Отправляем значение пароля в соответствующее поле
        self.send_keys_into_field(RecoverPageLocators.new_password_input_field, password)

    @allure.step('Click on "Recover" button')
    def click_on_recovery_button(self):  # Клик по кнопке "Восстановить"
        self.click_on_button(RecoverPageLocators.recover_button)

    @allure.step('Check of "Save" button being displayed')
    def save_button_check(self):  # Проверяем отображение кнопки "Сохранить"
        return self.check_element(RecoverPageLocators.save_button)

    @allure.step("Check for highlighting of Password field")
    def check_field_password_is_active(self, password):  # Проверяем, что поле пароля подсвечивается
        self.send_keys_to_password_field(password)
        self.click_on_button(RecoverPageLocators.show_password_button)
        return self.check_element(RecoverPageLocators.password_input_field_active)

