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

    @allure.step('Creating an order and getting its number')
    def make_order_and_get_order_number(self):
        self.wait_visibility_element(MainPageLocators.INGREDIENT_BUN)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)
        self.find_element(MainPageLocators.CREATE_ORDER_BTN)
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BTN)
        self.wait_visibility_element(MainPageLocators.ORDER_STATUS_TEXT)
        self.wait_invisibility_element(MainPageLocators.DEFAULT_ORDER_NUMBER)
        order = self.get_text_of_element(MainPageLocators.ORDER_NUMBER)
        self.move_to_element_and_click(MainPageLocators.CLOSE_BTN)
        return order
