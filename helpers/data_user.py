from faker import Faker
import allure


class PersonData:  # Создание корректных данных пользователя
    @staticmethod
    @allure.step('Generate name,email and password of user')
    def create_correct_user_data():
        faker = Faker('ru_RU')
        data = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.first_name()
        }
        return data
