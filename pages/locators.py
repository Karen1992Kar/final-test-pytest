from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_CLICK = (By.CSS_SELECTOR, "add_to_basket_form")


class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class BasketPageLocators():
    NAME_PRODUCT = (By.CSS_SELECTOR, "#messages .alert:first-child strong")




