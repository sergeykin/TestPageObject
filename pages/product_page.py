from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()


    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.find_element(*ProductPageLocators.BASKET_LINK), " error BASKET_LINK"

