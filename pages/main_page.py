import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Click the "Login to account" button')
    def click_on_enter_btn(self):
        self.move_to_element_and_click(MainPageLocators.ENTER_ACCOUNT_BTN)

    @allure.step('Click the "Fluorescent bun" ingredient')
    def click_on_bun(self):
        self.move_to_element_and_click(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Click the cross in the modal window')
    def click_close_btn(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_BTN)

    @allure.step('Click the "Place an order" button')
    def click_order_btn(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BTN)

    @allure.step('Adding a bun to the cart')
    def add_bun_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('Adding a filling to the cart')
    def add_filling_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)

    @allure.step('Add a sauce to the cart')
    def add_sauce_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.ORDER_BASKET)

    @allure.step('Getting the amount of added ingredient')
    def check_counter_of_ingredients(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_COUNTER)
    
    @allure.step('Check invisibility of popup')
    def check_invisibility_of_popup(self):
        return self.check_invisibility(MainPageLocators.INGREDIENT_POPUP)
    
    @allure.step('Check the popup text')
    def check_popup_text(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_POPUP_TITLE)
    
    @allure.step('Find the bun ingredient')
    def find_ingredient_bun(self):
        return self.find_element(MainPageLocators.INGREDIENT_BUN)
    
    @allure.step('Find the order number')
    def find_order_number(self):
        return self.find_element(MainPageLocators.ORDER_NUMBER)
    
    @allure.step('Check the order status')
    def check_order_status(self):
        return self.check_element(MainPageLocators.ORDER_STATUS_TEXT)
    
    @allure.step('Wait visibility the burger title')
    def wait_visibility_burger_title(self):
        return self.wait_visibility_element(MainPageLocators.BURGER_CONSTRUCTOR_TITLE)

    @allure.step('Creating an order and getting its number')
    def make_order_and_get_order_number(self):
        self.wait_visibility_element(MainPageLocators.INGREDIENT_BUN)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)
        self.find_element(MainPageLocators.CREATE_ORDER_BTN)
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BTN)
        self.wait_visibility_element(MainPageLocators.ORDER_STATUS_TEXT)
        self.check_invisibility(MainPageLocators.DEFAULT_ORDER_NUMBER)
        order = self.get_text_of_element(MainPageLocators.ORDER_NUMBER)
        self.move_to_element_and_click(MainPageLocators.CLOSE_BTN)
        return order
