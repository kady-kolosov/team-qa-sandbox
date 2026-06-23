from .base_page import BasePage
from .locators import PurchasesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PurchasesPage(BasePage):
    def should_be_purchases_header(self):
        assert self.is_element_present(
            *PurchasesPageLocators.PURCHASES_HEADER
        ), "❌ Не отображается страница покупок"

    def should_be_product_card(self):
        assert self.is_element_present(
            *PurchasesPageLocators.PRODUCT_CARDS
        ), "❌ Не отображаются карточки продукта"
