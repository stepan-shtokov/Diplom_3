import allure
import requests
from static_data.ingredients import Ingredients
from static_data.urls import MainPageURL, Endpoints


class Order:

    @allure.step('Create new order by API')  # Создание заказа через АПИ
    def create_order(self, create_user):
        token = create_user[1].json()['accessToken']
        header = {'Authorization': token}
        ingredients = Ingredients.correct_ingredients_data
        requests.post(MainPageURL.MAIN_URL + Endpoints.CREATE_ORDER, headers=header, data=ingredients)

    @allure.step('Get user orders by API')  # Получение заказов пользователя через АПИ
    def get_user_orders(self, create_user):
        token = create_user[1].json()['accessToken']
        header = {'Authorization': token}
        response = requests.get(MainPageURL.MAIN_URL + Endpoints.GET_ORDERS, headers=header)
        return response.json()['orders'][0]['number']
