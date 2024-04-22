import allure
from pages.header_page import HeaderPage
from data import Urls


class TestHeaderPage:
    @allure.title('Checking transition to "Constructor"')
    def test_redirect_to_constructor(self, driver):
        hp = HeaderPage(driver)
        hp.click_orders_list_btn()
        hp.click_constructor_btn()
        current_url = hp.get_current_url()
        assert current_url == Urls.MAIN_PAGE

    @allure.title('Checking the transition to the Order Feed')
    def test_redirect_to_order_list(self, driver):
        hp = HeaderPage(driver)
        hp.click_orders_list_btn()
        current_url = hp.get_current_url()
        assert current_url == Urls.FEED
