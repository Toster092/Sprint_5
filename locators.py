from selenium.webdriver.common.by import By

class TestLocators:
 LOGIN_BUTTON_LOCATOR = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]" # Локатор кнопки "Войти в аккаунт"

 REGISTER_BUTTON_LOCATOR = By.XPATH, "//a[contains(text(),'Зарегистрироваться')]" # Локатор кнопки "Зарегистрироваться"

 NAME_FIELD_LOCATOR = By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input[@name='name']" # Локатор поля "Имя"

 EMAIL_FIELD_LOCATOR = By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input[@name='name']" # Локатор поля "Email"

 PASSWORD_FIELD_LOCATOR = By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input[@name='Пароль']" # Локатор поля "Пароль"

 REGISTER_SUBMIT_BUTTON_LOCATOR = By.XPATH, "//button[contains(text(),'Зарегистрироваться')]" # Локатор кнопки подтверждения регистрации

 LOGIN_SUBMIT_BUTTON_LOCATOR = By.XPATH, "//button[contains(text(),'Войти')]" # Локатор кнопки "Войти"

 LOGIN_TITLE_LOCATOR = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/h2[1]" # Локатор заголовка "Вход"

 PASSWORD_ERROR_LOCATOR = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/p[1]" # Локатор сообщения "Некорректный пароль"

 ORDER_BUTTON_LOCATOR = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]" # Локатор кнопки "Оформить заказ"

 ACCOUNT_BUTTON_LOCATOR = By.XPATH, "//p[contains(text(),'Личный Кабинет')]" # Локатор кнопки "Личный кабинет"

 LOGIN_IN_REGISTER_LOCATOR = By.XPATH, "html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]" # Локатор кнопки "Войти" в форме регистрации

 FORGOT_PASSWORD_LOCATOR = By.XPATH, "//a[contains(text(),'Восстановить пароль')]" # Локатор кнопки "Восстановить пароль"

 FORGOT_PASSWORD_SUBMIT_LOCATOR = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]" # Локатор кнопки "Войти" в форме восстановления пароля

 ACCOUNT_PROFILE_LOCATOR = By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']" # Локатор кнопки "Профиль" в личном кабинете

 CONSTRUCTION_LOCATOR = By.XPATH, "//p[contains(text(),'Конструктор')]" # Локатор кнопки "Конструктор"

 BURGER_CONSTRUCTION_TITLE_LOCATOR = By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']" # Локатор заголовка "Соберите бургер"

 LOGO_LOCATOR = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/div[1]/a[1]/*" # Локатор логотипа "Stellar Burger"

 LOGOUT_LOCATOR = By.XPATH, "//button[contains(text(),'Выход')]"  # Локатор кнопки "Выход" в личном кабинете

 LOGIN_AFTER_LOGOUT_LOCATOR = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/button[1]" # Локатор кнопки "Войти" после выхода из личного кабинета

 SOUSSES_TAB_LOCATOR = By.XPATH, "//span[contains(text(),'Соусы')]" # Локатор вкладки "Соусы"

 BURGERS_TAB_LOCATOR = By.XPATH, "//span[contains(text(),'Булки')]" # Локатор вкладки "Булки"

 FLUORESCENT_BURGER_LOCATOR = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/ul[1]/a[1]/p[1]" # Локатор бургерной булки с флюоресцентным соусом R2-D3

 SOUSSE_SPIKY_X_LOCATOR = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/ul[2]/a[1]/p[1]" # Локатор Соус Spicy-X

 INGREDIENTS_TAB_LOCATOR = By.XPATH, "//span[contains(text(),'Начинки')]" # Локатор вкладки "Начинки"

 LIGHTNING_FILE_LOCATOR = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/ul[3]/a[4]/p[1]" # Локатор Филе Люминесцентного тетраодонтимформа
