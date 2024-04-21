import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Search')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Wait element to be clickable')
    def wait_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)
 
    @allure.step('Click the element')
    def click_to_element(self, locator):
        self.wait_element_to_be_clickable(locator).click()

    @allure.step('Getting the text of an element')
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Insert text {text}')
    def set_text_to_element(self, locator, text):
        self.wait_element_to_be_clickable(locator).send_keys(text)

    @allure.step('Click a visible element')
    def click_to_visible_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Checking whether an element is displayed on a page')
    def check_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Checking whether an element is invisible on a page')
    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(locator))

    @allure.step('Waiting for an element to be visible on the page')
    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Waiting for an element to be invisible on the page')
    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    @allure.step('Get the current link')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Open the page')
    def open_page(self, url):
        return self.driver.get(url)

    @allure.step('Waiting to open a new tab')
    def wait_open_new_tab(self, index):
        WebDriverWait(self.driver, 15).until(EC.number_of_windows_to_be(index))

    @allure.step('Waiting to open an {url}')
    def wait_open_page(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(url))

    @allure.step('Drag and Drop an element')
    def drag_and_drop_element(self, locator_from, locator_to):
        self.wait_visibility_element(locator_from)
        self.wait_visibility_element(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_from, element_to)

    @allure.step('Drag an element and click on them')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()
