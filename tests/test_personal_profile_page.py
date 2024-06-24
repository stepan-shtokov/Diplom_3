import allure

from static_data.urls import URLS, MainPageURL
from pages.main_page import HeaderMainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalProfilePage


class TestPersonalProfilePage:

    @allure.title('Go to PersonalProfile page test')
    @allure.description("""
    1. Create user by API;
    2. Go to main SB page;
    3. Login user;
    4. Click on personal account button;
    5. Verify that personal profile page form is displayed;
    6. Delete user by API.
    """)
    def test_go_to_personal_profile_page(self, driver, create_user, login_user):
        header = HeaderMainPage(driver)
        personal_profile = PersonalProfilePage(driver)
        header.click_on_personal_profile_button_in_header()
        assert personal_profile.check_personal_profile_visible()
        assert personal_profile.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_personal_profile)

    @allure.title('Go to OrderFeed page test')
    @allure.description('''
    1. Create user by API;
    2. Go to main SB page;
    3. Login user;
    4. Click on personal account button;
    5. Click on order feed button;
    6. Verify that order feed form displayed;
    7. Delete user by API.
    ''')
    def test_go_to_order_feed_page(self, driver, create_user, login_user):
        header = HeaderMainPage(driver)
        personal_profile = PersonalProfilePage(driver)
        header.click_on_personal_profile_button_in_header()
        personal_profile.click_on_orders_history_button()
        assert personal_profile.check_order_history_form()
        assert personal_profile.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_order_history)

    @allure.title('Test exit from account')
    @allure.description('''
    1. Create user by API;
    2. Go to main SB page;
    3. Login user;
    4. Click on personal account button;
    5. Click on exit button;
    6. Verify that exit is successful;
    7. Delete user by API.
    ''')
    def test_exit_from_personal_profile(self, driver, create_user, login_user):
        header = HeaderMainPage(driver)
        login_page = LoginPage(driver)
        personal_profile = PersonalProfilePage(driver)
        header.click_on_personal_profile_button_in_header()
        personal_profile.click_on_exit_button()
        assert login_page.check_presence_of_auth_form()
        assert login_page.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_login)
