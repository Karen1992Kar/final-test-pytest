from pages.main_page import MainPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
    time.sleep(5)


# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_should_see_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = LoginPage(browser, link)
#     page.open()
#     page1 = MainPage(browser, link)
#     page1.go_to_login_page()
#     page.should_be_login_page()



