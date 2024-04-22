import allure
from pages.main_page import MainPage
from data import Text


class TestMainPage:
    @allure.title('Checking the appearance of a pop-up window after clicking on an ingredient')
    def test_open_ingredient_popup(self, driver):
        mp = MainPage(driver)
        mp.click_on_bun()
        popup_text = mp.check_popup_text()
        assert popup_text == Text.POPUP_TEXT

    @allure.title('Checking the closing of the ingredient pop-up window by clicking the cross')
    def test_close_ingredient_details_popup(self, driver):
        mp = MainPage(driver)
        mp.click_on_bun()
        mp.click_close_btn()
        mp.check_invisibility_of_popup()
        assert mp.check_invisibility_of_popup().is_displayed() == False

    @allure.title('Checking for ingredient counter changes')
    def test_change_ingredient_counter(self, driver):
        mp = MainPage(driver)
        start_quantity = mp.check_counter_of_ingredients()
        mp.add_filling_to_order_basket()
        end_quantity = mp.check_counter_of_ingredients()
        assert end_quantity > start_quantity

    @allure.title('Checking order creation')
    def test_make_order(self, driver, login_user):
        mp = MainPage(driver)
        mp.find_ingredient_bun()
        mp.add_bun_to_order_basket()
        mp.add_sauce_to_order_basket()
        mp.click_order_btn()
        mp.find_order_number()
        assert mp.check_order_status().is_displayed()
