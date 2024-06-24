class MainPageURL:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'  # Базовый URL-адрес сервиса Stellar Burgers


class Endpoints:
    CREATE_USER = 'api/auth/register'  # Создание пользователя
    DELETE_USER = 'api/auth/user'  # Удаление пользователя
    LOGIN = 'api/auth/login'  # Логин пользователя
    CREATE_ORDER = 'api/orders'  # Создание заказа
    GET_ORDERS = 'api/orders'  # Получение заказов


class URLS:
    url_feed = 'feed'  # Лента
    url_register = 'register'  # Регистрация
    url_login = 'login'  # Логин
    url_recovery = 'forgot-password'  # Восстановление пароля
    url_personal_profile = 'account/profile'  # ЛК
    url_order_history = 'account/order-history'  # История заказов ЛК
    url_reset_password = 'reset-password'  # Сбросить пароль
