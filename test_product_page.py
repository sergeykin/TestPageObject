import pytest
import time
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=newYear"
LOGIN_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"


class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LOGIN_LINK)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "t,fnmvjq[eq")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.check_adding_message_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.add_product_to_cart()
        page.check_for_message_product_is_added()
        page.check_for_correct_cart_price()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.check_for_message_product_is_added()
    page.check_for_correct_cart_price()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.check_adding_message_not_present()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_url()
    cart_page.cart_is_empty()
    cart_page.should_be_empty_cart_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_url()
    page.should_be_login_form()