import allure
from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage


class OrdersPage(BasePage):
    @allure.step('Click an order in the Order Feed list')
    def click_order(self):
        self.click_to_visible_element(OrdersPageLocators.ORDER_LINK)

    @allure.step('Receiving an order by number in the Order Feed')
    def get_order_in_order_list(self, order):
        method, locator = OrdersPageLocators.ORDER_NUMBER
        locator = locator.format(order)
        return self.find_element((method, locator))

    @allure.step('Getting the number of orders completed over the entire period')
    def get_total_orders_number(self):
        return self.get_text_of_element(OrdersPageLocators.COMPLETED_ORDERS_TOTAL)

    @allure.step('Getting the number of orders completed today')
    def get_today_orders_number(self):
        return self.get_text_of_element(OrdersPageLocators.COMPLETED_ORDERS_TODAY)

    @allure.step('Receive an order by number in the "In progress" section')
    def get_order_number_in_work(self):
        return self.get_text_of_element(OrdersPageLocators.ORDER_IN_WORK)
    
    @allure.step('Wait visibility order in work')
    def wait_visibility_order_in_work(self):
        return self.wait_visibility_element(OrdersPageLocators.ORDER_IN_WORK)
    
    @allure.step('Check the order structure title')
    def check_order_structure_title(self):
        return self.check_element(OrdersPageLocators.ORDER_STRUCTURE_TITLE)
    
    @allure.step('Find the order list title')
    def find_order_list_title(self):
        return self.find_element(OrdersPageLocators.ORDERS_LIST_TITLE)
    
    @allure.step('Wait visibility the order list title')
    def wait_visibility_order_list_title(self):
        return self.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
