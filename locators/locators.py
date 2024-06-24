from selenium.webdriver.common.by import By


class HeaderLocators:
    constructor_button = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")  # Кнопка "Конструктор" хедера главной страницы
    order_feed_button = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")  # Кнопка "Лента заказов" хедера главной страницы
    personal_account_button = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")  # Кнопка "Личный Кабинет" хедера главной страницы


class MainPageLocators:
    feed_order_form = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")  # Форма ленты заказов
    constructor_form = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")  # Форма конструктора
    order_place_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка "Оформить заказ"
    fluorescent_bun_button = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")  # Флуоресцентная булочка в конструкторе
    closing_cross_button = (By.XPATH, '//button[contains(@class,"close")]')  # Иконка крестика модального окна ингредиентов
    order_form = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")  # Форма оформленного заказа
    order_basket = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")  # Корзина
    ingredient_counter = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")  # Счетчик кол-ва ингредиентов
    order_number = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")  # Номер заказа
    personal_account_login_button = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт" формы заказа
    popup_from_ingredient = (By.XPATH, "//h2[text()= 'Детали ингредиента']")  # Модальное окно сведений об ингредиенте


class AuthPageLocators:
    authorization_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Форма авторизации
    email_input_field = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email, авторизация
    password_input_field = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля, авторизация
    login_account_button = (By.XPATH, "//button[text() = 'Войти']")  # Поле ввода логина
    registration_button = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    recovery_button = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Кнопка "Восстановить пароль"


class RecoverPageLocators:
    email_input_field = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email, восстановление
    recover_button = (By.XPATH, "//button[text() = 'Восстановить']")  # Кнопка "Восстановить" окна восстановления
    login_account_button = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка "Войти" окна восстановления
    new_password_input_field = (By.XPATH, ".//input[@name = 'Введите новый пароль']")  # Поле ввода нового пароля
    code_from_email_input_field = (By.XPATH, ".//label[text() = 'Введите код из письма']")  # Поле "Введите код из письма" окна восстановления
    show_password_button = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")  # Кнопка "Показать пароль" поля пароля
    password_input_field_active = (By.CSS_SELECTOR, ".input.input_status_active")  # Активность поля "Пароль"
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка "Сохранить"
    recover_form_text = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")  # Текст "Восстановление пароля" окна восстановления


class PersonalProfileLocators:
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # Форма ЛК
    profile_button = (By.XPATH, ".//a[text() = 'Профиль']")  # Кнопка "Профиль" ЛК
    order_history_button = (By.XPATH, ".//a[text() = 'История заказов']")  # Кнопка "История заказов" ЛК
    order_history_form = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")  # Форма истории заказов ЛК
    order_number = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")  # Номер заказа
    cancel_button = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка "Отмена" ЛК
    exit_button = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка "Выход" ЛК
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка "Сохранить" ЛК


class OrderFeedLocators:
    orders_info = (By.XPATH, '//p[text()="Cостав"]')  # Окно с деталями заказа
    title_orders_feed = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок окна истории заказов
    counter_of_total_orders = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # Счетчик заказов "За все время"
    counter_of_daily_orders = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # Счетчик ежедневно выполненных заказов
    counter_of_orders_in_progress = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")  # Счетчик заказов "В работе"
    order_window_info = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")  # Локатор первого заказа в истории
    order_history_all = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')  # Все заказы в истории сервиса
