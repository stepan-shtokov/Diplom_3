import allure

from static_data.urls import URLS, MainPageURL
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage
from pages.login_page import LoginPage
from helpers.data_user import PersonData


class TestRecoveryPage:

    @allure.title('Test click on "Recover password" leads to password recovery page')
    @allure.description('''
    1. Go to main SB page;
    2. Go to personal profile page;
    3. Click on recover password button.
    ''')
    def test_recover_password_button(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_personal_account_button_mainpage()
        login_page.click_on_recovery_button()
        assert recovery_page.check_recovery_form()
        assert recovery_page.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_recovery)

    @allure.title('Test click on show password button makes field active')
    @allure.description('''
    1. Go to SB main page;
    2. Go to personal profile page;
    3. Click on recover password button;
    4. Filling email input field;
    5. Click on recover button;
    6. Filling password input field;
    7. Click on show password button.
    ''')
    def test_check_highlighting_of_password_field(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        user_data = PersonData().create_correct_user_data()
        main_page.click_on_personal_account_button_mainpage()
        login_page.click_on_recovery_button()
        recovery_page.send_keys_to_email_field(user_data.get('email'))
        recovery_page.click_on_recovery_button()
        assert recovery_page.check_field_password_is_active(user_data.get('password'))

    @allure.title('Test email input and click on recover button')
    @allure.description('''
    1. Go to main SB page;
    2. Go to personal account page;
    3. Click on recover password button;
    4. Filling email in email input field;
    5. Click on recover button.
    ''')
    def test_email_input_and_recover_button_click(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_personal_account_button_mainpage()
        login_page.click_on_recovery_button()
        recovery_page.send_keys_to_email_field(PersonData().create_correct_user_data()['email'])
        recovery_page.click_on_recovery_button()
        assert recovery_page.save_button_check()
        assert recovery_page.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_reset_password)
