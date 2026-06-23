from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class AuthPageLocators:
    LOGIN_BTN = (By.CSS_SELECTOR, "header [class*='MenuLinks_authLink']")

    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "#checking-email-input",
    )
    CONTINUE_BTN = (
        By.XPATH,
        "//button[@type='button' and normalize-space()='Продолжить']",
    )

    # * Локаторы для регистрации
    SIGNUP_PASSWORD_INPUT = (By.CSS_SELECTOR, "#signup-password-input")
    AGREEMENT_CHECKBOX = (By.CSS_SELECTOR, "input#agreement[name='agreement']")
    PERSONAL_DATA_CHECKBOX = (
        By.CSS_SELECTOR,
        "input#personal_data[name='personalData']",
    )
    SIGNUP_BTN = (
        By.XPATH,
        "//button[@type='button' and normalize-space()='Зарегистрироваться']",
    )
    PAYWALL_FORM = (
        By.CSS_SELECTOR,
        "[class*='Advantages_content'] [class*='Tariff_tariff']",
    )
    CLOSE_PAYWALL_FORM = (By.CSS_SELECTOR, "[class*='AuthWrapper_close']")

    # * Локаторы для авторизации
    SIGNIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#signin-password-input")
    SIGNIN_BTN = (
        By.XPATH,
        "//button[@type='button' and normalize-space()='Войти']",
    )

    PROFILE_AVATAR = (By.CSS_SELECTOR, "header img[class*='Profile_profile__img']")
    BURGER_MENU = (By.CSS_SELECTOR, "header [class*='MenuBurger_burger']")


class SettingsPage:
    HEADER_IN_SETTING_ITEMS = (By.CSS_SELECTOR, "h1[class*='SettingsHeader_title']")


class PurchasesPageLocators:
    PURCHASES_HEADER = SettingsPage.HEADER_IN_SETTING_ITEMS
    PRODUCT_CARDS = (
        By.CSS_SELECTOR,
        "[class*='SettingsPurchase_vod'] [class*='SettingsPurchase_otherTypeItems']",
    )
