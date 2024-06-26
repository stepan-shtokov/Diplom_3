import pytest
import allure

from pages.main_page import HeaderMainPage
from pages.order_feed_page import OrderFeedPage
from helpers.helpers import Order
from locators.locators import OrderFeedLocators


class TestOrderFeedPage:

    @allure.title('Test click on order opens info window')
    @allure.description('''
    1. Go to main SB page;
    2. Click on order feed button;
    3. Click on order;
    4. Verify that info window is visible.
    ''')
    def test_check_info_window(self, driver):
        header = HeaderMainPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_on_order_feed_button_in_header()
        feed_order.click_on_order()
        assert feed_order.check_order_info()

    @allure.title('Test after new order counters of all and daily orders increases')
    @allure.description('''
    1. Create user by API;
    2. Go to main SB page;
    3. Login user;
    4. Go to order feed page;
    5. Get current amount of counter;
    6. Request to make order by API;
    7. Check that counter increased;
    8. Delete user by API.
    ''')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.counter_of_daily_orders,
                                         OrderFeedLocators.counter_of_total_orders])
    def test_order_counter_updated(self, driver, create_user, login_user, counter):
        order = Order()
        feed_order = OrderFeedPage(driver)
        header = HeaderMainPage(driver)
        header.click_on_order_feed_button_in_header()
        current_counter = int(feed_order.check_orders_counter(counter))
        order.create_order(create_user)
        updated_counter = int(feed_order.check_orders_counter(counter))
        assert updated_counter > current_counter

    @allure.title('Test order number appears in "In progress"')
    @allure.description("""
    1. Create user by API
    2. Go to main SB page;
    3. Login user;
    4. Go to order feed page;
    5. Get list of orders in progress;
    6. Get list of user orders;
    7. Verify that user order in "In progress" list;
    8. Delete user by API.
    """)
    def test_check_order_by_user_in_progress(self, driver, create_user, login_user):
        order = Order()
        header = HeaderMainPage(driver)
        order_feed = OrderFeedPage(driver)
        header.click_on_order_feed_button_in_header()
        order.create_order(create_user)
        orders_in_progress = order_feed.get_orders_in_progress()
        user_order = str(order.get_user_orders(create_user))
        assert user_order in orders_in_progress

    @allure.title('Test user orders from orders history appears in order feed')
    @allure.description('''
    1. Create user by API;
    2. Create order by API;
    3. Login user;
    4. Go to SB main page;
    5. Get user orders by API;
    6. Get list of orders in order feed;
    7. Verify that user order appears in order feed;
    8. Delete user by API.
    ''')
    def test_check_order_by_user_appears_in_history(self, driver, create_user, create_new_order, login_user):
        order = Order()
        feed_order = OrderFeedPage(driver)
        header = HeaderMainPage(driver)
        header.click_on_order_feed_button_in_header()
        user_order = str(order.get_user_orders(create_user))
        history_of_orders = feed_order.get_history_of_orders()
        assert user_order in history_of_orders
