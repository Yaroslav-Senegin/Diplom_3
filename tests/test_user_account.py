import allure
from data import Urls
from pages.user_account_page import UserAccountPage
from pages.header_page import HeaderPage
from data import Text
from locators.user_account_locators import UserAccountLocators


class TestUserAccount:
    @allure.title('Checking the transition to your personal account through the "Personal Account" button in the header')
    def test_redirect_to_account_from_header(self, driver, login_user):
        uap = UserAccountPage(driver)
        uap.click_account_btn()
        assert uap.get_current_url() == Urls.PROFILE_PAGE

    @allure.title('Checking the transition to the Order History section')
    def test_redirect_to_order_history(self, driver, login_user):
        uap = UserAccountPage(driver)
        uap.click_account_btn()
        uap.click_on_order_list()
        assert uap.get_current_url() == Urls.ORDERS_HISTORY

    @allure.title('Verifying logout')
    def test_logout(self, driver, login_user):
        uap = UserAccountPage(driver)
        HeaderPage(driver).click_user_account_btn()
        uap.wait_visibility_profile_button()
        uap.click_logout_btn()
        uap.wait_visibility_enter_button()
        assert uap.get_text_enter_button() == Text.BUTTON_TEXT
