import allure
from locators.user_account_locators import UserAccountLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class UserAccountPage(BasePage):
    @allure.step('Click the "Recover Password" button')
    def click_password_recover_btn(self):
        self.click_to_visible_element(UserAccountLocators.RESET_PASSWORD_BTN)

    @allure.step('Check visibility the profile button')
    def wait_visibility_profile_button(self):
        return self.wait_visibility_element(UserAccountLocators.PROFILE_BTN)    
    
    @allure.step('Check visibility the enter button')
    def wait_visibility_enter_button(self):
        self.wait_visibility_element(UserAccountLocators.ENTER_BTN)

    @allure.step('Check text the enter button')
    def get_text_enter_button(self):
        return self.get_text_of_element(UserAccountLocators.ENTER_BTN)

    @allure.step('Click the Personal Account button')
    def click_account_btn(self):
        self.move_to_element_and_click(HeaderLocators.ACCOUNT_BTN)
        self.wait_visibility_profile_button()

    @allure.step('Click the "Exit" button')
    def click_logout_btn(self):
        self.click_to_visible_element(UserAccountLocators.EXIT_BTN)

    @allure.step('Click the "Order History" button"')
    def click_on_order_list(self):
        self.click_to_visible_element(UserAccountLocators.ORDERS_HISTORY_BTN)

    @allure.step('Getting the order number in "Order History"')
    def get_order_number(self):
        return self.get_text_of_element(UserAccountLocators.ORDER_NUMBER)
    
    @allure.step('Authorization')
    def login_user(self, user_data):
        self.set_text_to_element(UserAccountLocators.INPUT_EMAIL, user_data['email'])
        self.set_text_to_element(UserAccountLocators.INPUT_PASSWORD, user_data['password'])
        self.click_to_visible_element(UserAccountLocators.ENTER_BTN)

    @allure.step('Find the order status')
    def find_order_status(self):
        return self.find_element(UserAccountLocators.ORDER_STATUS)

