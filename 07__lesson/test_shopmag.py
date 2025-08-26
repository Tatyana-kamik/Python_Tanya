import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from shopmag_page import LoginPage, ShopPage, CartPage, CheckoutPage


@pytest.fixture
def web_driver():
    # Установка параметров для Firefox
    driver = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_saucedemo_checkout_with_pom(web_driver):
    login_url = "https://www.saucedemo.com/"

    # Авторизация
    login_page = LoginPage(web_driver)
    login_page.open(login_url)
    login_page.input_username("standard_user")
    login_page.input_password("secret_sauce")
    login_page.click_login()

    # Добавление товаров в корзину
    shop_page = ShopPage(web_driver)
    shop_page.add_to_cart_by_product_id("add-to-cart-sauce-labs-backpack")
    web_driver.execute_script("window.scrollBy(0, 100);")
    shop_page.add_to_cart_by_product_id("add-to-cart-sauce-labs-bolt-t-shirt")
    web_driver.execute_script("window.scrollBy(0, 400);")
    shop_page.add_to_cart_by_product_id("add-to-cart-sauce-labs-onesie")
    web_driver.execute_script("window.scrollTo(0, 0)")

    # Переход в корзину
    shop_page.go_to_cart()

    # Переход к оформлению заказа
    cart_page = CartPage(web_driver)
    cart_page.click_checkout()

    # Заполнение формы
    checkout_page = CheckoutPage(web_driver)
    checkout_page.fill_customer_info("Имя", "Фамилия", "12345")

    # Получение итоговой стоимости
    total_text = checkout_page.get_total()

    # Проверка итоговой суммы
    assert total_text == "Total: $58.29", f"Итоговая сумма $58.29, но была {
        total_text}"
