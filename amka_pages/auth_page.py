from .config import AmkaConfig
from .base_page import BasePage
from .locators import AuthPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AuthPage(BasePage):
    def guest_can_signup(self):
        """Данный метод вызывает методы регистрации и генирирует данные для нового
        пользователя"""
        email, password = AmkaConfig.generate_credentials()
        self.should_be_login_button()
        self.go_to_login_form()
        self.should_be_login_form()
        self.guest_entered_email(email)
        self.should_be_clickable_continue_btn()
        self.guest_click_to_continue_btn()
        self.should_be_signup_form()
        self.guest_entered_signup_password(password)
        self.guest_user_checked_checkboxes()
        self.guest_click_to_signup_btn()
        self.should_be_paywall_form()
        self.user_close_paywall_form()
        self.should_be_avatar_and_burger()

    def user_can_signin(self):
        """Данный метод вызывает методы авторизации с уже имеющимися данными"""
        email, password = AmkaConfig.AMKA_AUTH_USERNAME, AmkaConfig.AMKA_AUTH_PASSWORD
        self.should_be_login_button()
        self.go_to_login_form()
        self.should_be_login_form()
        self.guest_entered_email(email)
        self.should_be_clickable_continue_btn()
        self.guest_click_to_continue_btn()
        self.should_be_signin_form()
        self.user_entered_signin_password(password)
        self.user_click_to_signin_btn()
        self.should_be_avatar_and_burger()

    def should_be_login_button(self):
        assert self.is_element_present(
            *AuthPageLocators.LOGIN_BTN
        ), "❌ Не отображается кнопка авторизации"

    def go_to_login_form(self, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(AuthPageLocators.LOGIN_BTN)
            ).click()
        except TimeoutException as error:
            raise AssertionError("❌ Не удалось открыть форму авторизации") from error

    def should_be_login_form(self):
        assert self.is_element_present(
            *AuthPageLocators.EMAIL_INPUT
        ), "❌ Не отображается форма авторизации"

    def guest_entered_email(self, email, timeout=5):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(AuthPageLocators.EMAIL_INPUT)
        ).send_keys(email)

    def should_be_clickable_continue_btn(self):
        assert self.is_element_clickable(
            *AuthPageLocators.CONTINUE_BTN
        ), "❌ Кнопка 'Продолжить' не кликабельна"

    def guest_click_to_continue_btn(self, timeout=5):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(AuthPageLocators.CONTINUE_BTN)
        ).click()

    # * Регистрация
    def should_be_signup_form(self):
        assert self.is_element_present(
            *AuthPageLocators.SIGNUP_PASSWORD_INPUT
        ), "❌ Не отображается форма ввода пароля при регистрации"

    def guest_entered_signup_password(self, password, timeout=5):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(AuthPageLocators.SIGNUP_PASSWORD_INPUT)
        ).send_keys(password)

    def guest_user_checked_checkboxes(self, timeout=5):
        agreement_checkbox = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(AuthPageLocators.AGREEMENT_CHECKBOX)
        )
        self.browser.execute_script("arguments[0].click();", agreement_checkbox)

        personal_data_checkbox = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(AuthPageLocators.PERSONAL_DATA_CHECKBOX)
        )
        self.browser.execute_script("arguments[0].click();", personal_data_checkbox)

    def guest_click_to_signup_btn(self, timeout=5):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(AuthPageLocators.SIGNUP_BTN)
        ).click()

    def should_be_paywall_form(self):
        assert self.is_element_present(
            *AuthPageLocators.PAYWALL_FORM
        ), "❌ Не отображается окно с выбором тарифов"

    def user_close_paywall_form(self, timeout=5):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(AuthPageLocators.CLOSE_PAYWALL_FORM)
        ).click()

    def should_be_avatar_and_burger(self):
        assert self.is_element_present(
            *AuthPageLocators.PROFILE_AVATAR
        ), "❌ Нет аватара пользователя"
        assert self.is_element_present(
            *AuthPageLocators.BURGER_MENU
        ), "❌ Нет бургер меню"

    # * Аторизация
    def should_be_signin_form(self):
        assert self.is_element_present(
            *AuthPageLocators.SIGNIN_PASSWORD_INPUT
        ), "❌ Не отображается форма ввода пароля при авторизации"

    def user_entered_signin_password(self, password, timeout=5):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(AuthPageLocators.SIGNIN_PASSWORD_INPUT)
        ).send_keys(password)

    def user_click_to_signin_btn(self, timeout=5):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(AuthPageLocators.SIGNIN_BTN)
        ).click()
