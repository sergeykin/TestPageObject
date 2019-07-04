from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_cart_url(self):
        assert "/basket" in self.browser.current_url, "Current URL is not basket URL"

    def cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.ITEM_IN_CART, timeout=2)

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE)
        message = self.browser.find_element(*CartPageLocators.EMPTY_CART_MESSAGE).text
        assert "Your basket is empty." in message