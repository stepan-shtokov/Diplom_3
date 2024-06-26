import allure

from locators.locators import PersonalProfileLocators
from pages.base_page import BasePage


class PersonalProfilePage(BasePage):

    @allure.step('Click on "Orders history" button')  # Клик по кнопке "История заказов"
    def click_on_orders_history_button(self):
        self.click_on_button(PersonalProfileLocators.order_history_button)

    @allure.step("Click on 'Exit' button")  # Клик по кнопке "Выход"
    def click_on_exit_button(self):
        self.click_on_button(PersonalProfileLocators.exit_button)

    @allure.step("Check for 'Orders history' being displayed")  # Проверяем отображение истории заказов
    def check_order_history_form(self):
        return self.check_element(PersonalProfileLocators.order_history_form)

    @allure.step('Check personal profile page form is visible')  # Проверяем отображение формы ЛК
    def check_personal_profile_visible(self):
        return self.check_element(PersonalProfileLocators.profile_form)
