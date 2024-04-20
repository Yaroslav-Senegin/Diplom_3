import allure
from data import Urls
from locators.password_recovery_locators import PasswordRecoverLocators
from pages.user_account_page import UserAccountPage
from pages.password_recovery_page import PasswordRecoverPage
from pages.header_page import HeaderPage


class TestPasswordRecover:
    @allure.title('Checking the transition by clicking on the Recover password button on the login page')
    def test_click_password_recover_button(self, driver):
        prp = PasswordRecoverPage(driver)
        HeaderPage(driver).click_user_account_btn()
        UserAccountPage(driver).click_password_recover_btn()
        prp.click_recover_btn()
        assert prp.find_element(PasswordRecoverLocators.SAVE_BTN).is_displayed()

    @allure.title('Checking the transition to the Restore button after entering email')
    def test_enter_email_and_click_recover(self, driver, user_data):
        prp = PasswordRecoverPage(driver)
        prp.open_page(Urls.FORGOT_PASSWORD_PAGE)
        prp.set_email_for_recover_password(user_data)
        prp.click_recover_btn()
        assert prp.find_element(PasswordRecoverLocators.SAVE_BTN).is_displayed()

    @allure.title('Checking the password field activity after clicking on the show/hide icon')
    def test_active_password_field(self, driver, user_data):
        prp = PasswordRecoverPage(driver)
        prp.open_page(Urls.FORGOT_PASSWORD_PAGE)
        prp.set_email_for_recover_password(user_data)
        prp.click_recover_btn()
        prp.find_element(PasswordRecoverLocators.SAVE_BTN)
        prp.click_on_show_password_icon()
        assert prp.find_element(PasswordRecoverLocators.INPUT_PASSWORD_ACTIVE)
