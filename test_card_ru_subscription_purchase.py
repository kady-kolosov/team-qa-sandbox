# pytest -s -v --tb=line test_card_ru_subscription_purchase.py
import pytest
from amka_pages.config import AmkaConfig
from amka_pages.auth_page import AuthPage
from amka_pages.purchases_page import PurchasesPage


# pytest -s -v --tb=line -m need_review
@pytest.mark.need_review
def test_guest_can_signup_from_main_page(browser):
    auth_page = AuthPage(browser, AmkaConfig.BASE_URL)
    auth_page.open_page()
    auth_page.guest_can_signup()


# pytest -s -v --tb=line -m need_review
@pytest.mark.need_review
def test_guest_can_signin_from_main_page(browser):
    auth_page = AuthPage(browser, AmkaConfig.BASE_URL)
    auth_page.open_page()
    auth_page.user_can_signin()


# pytest -s -v --tb=line -m new_user_card_ru_subscription_purchase
@pytest.mark.new_user_card_ru_subscription_purchase
class TestNewUsertCanSubscribeToAmediatekaAndKino1Tv:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        auth_page = AuthPage(browser, AmkaConfig.BASE_URL)
        auth_page.open_page()
        auth_page.guest_can_signup()

    def test_user_can_subscribe_to_amediateka(self, browser):
        purchases_page = PurchasesPage(
            browser, AmkaConfig.BASE_URL + "settings/purchase"
        )
        purchases_page.open_page()
        purchases_page.should_be_purchases_header()
        purchases_page.should_be_product_card()
