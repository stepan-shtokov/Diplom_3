# Дипломный проект, задание 3: UI

Автотесты сервиса  "Stellar Burgers". 
Сайт: `https://stellarburgers.nomoreparties.site/`

## Файлы:
- allure_results - Отчет о тестировании

- tests/test_main_page.py - Тесты главной страницы 
- tests/test_order_feed.py - Тесты ленты заказов
- tests/test_personal_profile_area.py - Тесты ЛК пользователя
- tests/test_recovery_page.py - Тесты страницы восстановления

- locators/locators.py - Локаторы

- helpers/data_user.py - Генераторы данных пользователя
- helpers/helpers.py - Создание и получение заказа по API

- static_data/urls - URL и эндпоинты сервиса Stellar Burgers
- static_data/ingredients.py -  Данные об ингредиентах



- pages/base_page.py - Базовые(общие) методы
- pages/login_page.py - Методы страницы логина
- pages/main_page.py - Методы главной страницы
- pages/order_feed_page.py - Методы ленты заказов
- pages/personal_account_page.py - Методы страницы ЛК пользователя
- pages/recovery_page.py - файл взаимодействия со страницей восстановления пароля

- requirements.txt - Файл с зависимостями
- conftest.py - Фикстуры, используемые в тестах

Перед работой с репозиторием требуется установить зависимости: 
```
pip install -r requirements.txt
```
Запустить тесты:
```
pytest tests --alluredir=allure_results
```
Просмотреть отчет о тестировании:
```
allure serve allure_results
```