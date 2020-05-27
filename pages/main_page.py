from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import BasketPageLocators


class MainPage(BasePage):

    def expected_result(self):
        name_product = self.browser.find_element_by_tag_name('h1').text
        name_expected_result = self.browser.find_element(*BasketPageLocators.NAME_PRODUCT).text
        assert name_expected_result == name_product, "do not match name"

    def go_to_basket_page(self):
        link1 = self.browser.find_element_by_id('add_to_basket_form')
        link1.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

