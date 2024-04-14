import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Checking the appearance of a pop-up window after clicking on an ingredient')
    def test_open_ingredient_popup(self, driver):
        mp = MainPage(driver)
        mp.click_on_bun()
        popup_text = mp.get_text_of_element(MainPageLocators.INGREDIENT_POPUP_TITLE)
        assert popup_text == "Детали ингредиента"

    @allure.title('Checking the closing of the ingredient pop-up window by clicking the cross')
    def test_close_ingredient_details_popup(self, driver):
        mp = MainPage(driver)
        mp.click_on_bun()
        mp.click_close_btn()
        mp.check_invisibility(MainPageLocators.INGREDIENT_POPUP)
        assert mp.check_element(MainPageLocators.INGREDIENT_POPUP).is_displayed() == False

    @allure.title('Checking for ingredient counter changes')
    def test_change_ingredient_counter(self, driver):
        mp = MainPage(driver)
        start_quantity = mp.check_counter_of_ingredients()
        mp.add_filling_to_order_basket()
        end_quantity = mp.check_counter_of_ingredients()
        assert end_quantity > start_quantity

    @allure.title('Checking order creation')
    def test_make_order(self, driver, login):
        mp = MainPage(driver)
        mp.find_element(MainPageLocators.INGREDIENT_BUN)
        mp.add_bun_to_order_basket()
        mp.add_sauce_to_order_basket()
        mp.click_order_btn()
        mp.find_element(MainPageLocators.ORDER_NUMBER)
        assert mp.check_element(MainPageLocators.ORDER_STATUS_TEXT).is_displayed() == True
