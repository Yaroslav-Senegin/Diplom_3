import allure
from pages.orders_page import OrdersPage
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.user_account_page import UserAccountPage


class TestOrderListPage:
    @allure.title('Checking the pop-up window with order details')
    def test_open_order_details_popup(self, driver):
        op = OrdersPage(driver)
        HeaderPage(driver).click_orders_list_btn()
        op.click_order()
        assert op.check_order_structure_title().is_displayed()

    @allure.title('Checking whether the created order is displayed in the Order list')
    def test_new_order_in_order_list(self, driver, login_user):
        mp = MainPage(driver)
        hp = HeaderPage(driver)
        ap = UserAccountPage(driver)
        op = OrdersPage(driver)
        mp.make_order_and_get_order_number()
        ap.click_account_btn()
        ap.click_on_order_list()
        ap.find_order_status()
        order_number = ap.get_order_number()
        hp.click_orders_list_btn()
        op.find_order_list_title()
        wanted_order = op.get_order_in_order_list(order_number)
        assert wanted_order.is_displayed()

    @allure.title('Checking the "All Time Completed" counter changes after creating an order')
    def test_change_counter_total_orders(self, driver, login_user):
        mp = MainPage(driver)
        hp = HeaderPage(driver)
        op = OrdersPage(driver)
        mp.find_ingredient_bun()
        hp.click_orders_list_btn()
        op.wait_visibility_order_list_title()
        total_number = op.get_total_orders_number()
        hp.click_constructor_btn()
        mp.wait_visibility_burger_title()
        mp.make_order_and_get_order_number()
        hp.click_orders_list_btn()
        op.wait_visibility_order_list_title()
        new_total_number = op.get_total_orders_number()
        assert int(new_total_number) == int(total_number) + 1

    @allure.title('Checking the "Completed for Today" counter changes after creating an order')
    def test_change_counter_today_orders(self, driver, login_user):
        mp = MainPage(driver)
        hp = HeaderPage(driver)
        op = OrdersPage(driver)
        mp.find_ingredient_bun()
        hp.click_orders_list_btn()
        op.wait_visibility_order_list_title()
        today_number = op.get_today_orders_number()
        hp.click_constructor_btn()
        mp.wait_visibility_burger_title()
        mp.make_order_and_get_order_number()
        hp.click_orders_list_btn()
        op.wait_visibility_order_list_title()
        new_number = op.get_today_orders_number()
        assert int(new_number) == int(today_number) + 1

    @allure.title('Checking whether a new order is displayed in the "In Progress" list')
    def test_new_order_appears_in_work_list(self, driver, login_user):
        mp = MainPage(driver)
        hp = HeaderPage(driver)
        op = OrdersPage(driver)
        new_order = mp.make_order_and_get_order_number()
        hp.click_orders_list_btn()
        op.wait_visibility_order_in_work()
        order_in_work = op.get_order_number_in_work()
        assert new_order in order_in_work
