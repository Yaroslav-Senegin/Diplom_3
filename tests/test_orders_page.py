import allure
from locators.orders_page_locators import OrdersPageLocators
from locators.user_account_locators import UserAccountLocators
from locators.main_page_locators import MainPageLocators
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
        assert op.check_element(OrdersPageLocators.ORDER_STRUCTURE_TITLE).is_displayed()

    @allure.title('Checking whether the created order is displayed in the Order list')
    def test_new_order_in_orderlist(self, driver, login_user):
        mp = MainPage(driver)
        hp = HeaderPage(driver)
        ap = UserAccountPage(driver)
        op = OrdersPage(driver)
        mp.make_order_and_get_order_number()
        ap.click_account_btn()
        ap.click_on_order_list()
        ap.find_element(UserAccountLocators.ORDER_STATUS)
        order_number = ap.get_order_number()
        hp.click_orders_list_btn()
        op.find_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        wanted_order = op.get_order_in_orderlist(order_number)
        assert wanted_order.is_displayed()

    @allure.title('Checking the "All Time Completed" counter changes after creating an order')
    def test_change_counter_total_orders(self, driver, login_user):
        mp = MainPage(driver)
        hp = HeaderPage(driver)
        op = OrdersPage(driver)
        mp.find_element(MainPageLocators.INGREDIENT_BUN)
        hp.click_orders_list_btn()
        op.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        total_number = op.get_total_orders_number()
        hp.click_constructor_btn()
        mp.wait_visibility_element(MainPageLocators.BURGER_CONSTRUCTOR_TITLE)
        mp.make_order_and_get_order_number()
        hp.click_orders_list_btn()
        op.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        new_total_number = op.get_total_orders_number()
        assert int(new_total_number) == int(total_number) + 1

    @allure.title('Checking the "Completed for Today" counter changes after creating an order')
    def test_change_counter_today_orders(self, driver, login_user):
        mp = MainPage(driver)
        hp = HeaderPage(driver)
        op = OrdersPage(driver)
        mp.find_element(MainPageLocators.INGREDIENT_BUN)
        hp.click_orders_list_btn()
        op.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        today_number = op.get_today_orders_number()
        hp.click_constructor_btn()
        mp.wait_visibility_element(MainPageLocators.BURGER_CONSTRUCTOR_TITLE)
        mp.make_order_and_get_order_number()
        hp.click_orders_list_btn()
        op.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        new_number = op.get_today_orders_number()
        assert int(new_number) == int(today_number) + 1

    @allure.title('Checking whether a new order is displayed in the "In Progress" list')
    def test_new_order_appears_in_work_list(self, driver, login_user):
        mp = MainPage(driver)
        hp = HeaderPage(driver)
        op = OrdersPage(driver)
        new_order = mp.make_order_and_get_order_number()
        hp.click_orders_list_btn()
        op.wait_visibility_element(OrdersPageLocators.ALL_ORDERS_READY)
        op.wait_visibility_element(OrdersPageLocators.ORDER_IN_WORK)
        order_in_work = op.get_order_number_in_work()
        assert new_order in order_in_work
