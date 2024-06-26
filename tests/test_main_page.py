import allure

from static_data.urls import URLS, MainPageURL
from pages.main_page import MainPage, HeaderMainPage


class TestMainPage:

    @allure.title('Check proceeding to constructor')
    @allure.description("""
    1. Go to main SB page;
    2. Click on personal acc button;
    3. Click on Constructor button;
    4. Verify displaying of constructor form.
    """)
    def test_proceeding_to_constructor(self, driver):
        header = HeaderMainPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button_mainpage()
        header.click_on_construction_button_in_header()
        assert main_page.check_constructor_form() and main_page.get_current_url() == MainPageURL.MAIN_URL

    @allure.title('Check proceeding to order feed')
    @allure.description("""
    1. Go to main SB page;
    2. Click on order feed button;
    3. Verify displaying of order feed form.
    """)
    def test_proceeding_to_order_feed(self, driver):
        header = HeaderMainPage(driver)
        main_page = MainPage(driver)
        header.click_on_order_feed_button_in_header()
        assert main_page.check_order_feed_form() and main_page.get_current_url() == (MainPageURL.MAIN_URL + URLS.url_feed)

    @allure.title('Test of info window popup after click on ingredient')
    @allure.description('''
    1. Go to main SB page;
    2. Click on fluorescent bun;
    3. Verify that info popup about bun is displayed.
    ''')
    def test_check_bun_info_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_in_constructor()
        assert main_page.check_bun_info_displayed()

    @allure.title('Test of closing info window')
    @allure.description('''
    1. Go to main SB page;
    2. Click on fluorescent bun;
    3. Click on closure cross of modal window;
    4. Verify that window is closed.
    ''')
    def test_check_bun_info_window_closed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_in_constructor()
        main_page.close_info_popup()
        assert main_page.check_close_bun_info()

    @allure.title('Ingredient counter increases test')
    @allure.description('''
    1. Go to main SB page;
    2. Add bun to basket;
    3. Verify that counter increases.
    ''')
    def test_ingredient_counter_increases(self, driver):  # Этот тест требует наличия seletools(JS-имитация перетаскивания)
        main_page = MainPage(driver)
        main_page.bun_add_to_basket()
        assert int(main_page.get_number_of_ingredients_in_order()) > 0

    @allure.title('Logged user can place order test')
    @allure.description('''
    1. Create a user by API;
    2. Go to main SB page;
    3. Login user;
    4. Add bun to basket;
    5. Click on place order button;
    6. Check for order form being visible;
    7. Delete user by API.
    ''')
    def test_create_order_by_logged_user(self, driver, create_user, login_user):
        main_page = MainPage(driver)
        header = HeaderMainPage(driver)
        header.click_on_construction_button_in_header()
        main_page.create_an_order()
        assert main_page.check_order_form_being_displayed()
