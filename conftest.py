import pytest
from selenium import webdriver
from helpers import *
from locators.user_account_locators import UserAccountLocators
from locators.header_locators import HeaderLocators
from pages.main_page import MainPage
from pages.user_account_page import UserAccountPage
import requests
from data import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture()
def user_data():
    user_data = create_user_data()
    response = requests.post(Urls.REGISTER_USER, user_data)
    yield user_data
    headers = {'Authorization': response.json()['accessToken']}
    requests.delete(Urls.DELETE_USER, headers=headers)

@pytest.fixture()
def login_user(driver, user_data):
    MainPage(driver).click_on_enter_btn()
    UserAccountPage(driver).login_user(user_data)


