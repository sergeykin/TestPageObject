import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage


MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_link(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_url()
    cart_page.cart_is_empty()
    cart_page.should_be_empty_cart_message()


def test_guest_can_go_to_login_link(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_url()
    page.should_be_login_form()