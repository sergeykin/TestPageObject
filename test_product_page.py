from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_cart(browser):
    promoCod = "?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/" + promoCod
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу

    product_page = ProductPage(browser, browser.current_url)
    time.sleep(3)
    product_page.should_be_basket_page()
    time.sleep(3)
    product_page.solve_quiz_and_get_code()
    # login_page = page.go_to_login_page()
    # login_page.should_be_login_page()