import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from shopmag_page import LoginPage, ShopPage, CartPage, CheckoutPage


@pytest.fixture
def web_driver():
    """
    Фикстура для создания и закрытия Firefox WebDriver.

    :return: WebDriver - объект браузера Firefox.
    """
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Тест оформления заказа на сайте SauceDemo с использованием POM")
@allure.description(
    "Процесс авторизации, добавления товаров в корзину, оформления заказа и проверки итоговой суммы."
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_checkout_with_pom(web_driver):
    login_url = "https://www.saucedemo.com/"

    login_page = LoginPage(web_driver)
    with allure.step("Открыть страницу входа на сайт"):
        login_page.open(login_url)

    with allure.step("Ввести имя пользователя и пароль"):
        login_page.input_username("standard_user")
        login_page.input_password("secret_sauce")

    with allure.step("Нажать кнопку входа (Login)"):
        login_page.click_login()

    shop_page = ShopPage(web_driver)

    with allure.step("Добавить товар 'Sauce Labs Backpack' в корзину"):
        shop_page.add_to_cart_by_product_id("add-to-cart-sauce-labs-backpack")

    with allure.step("Прокрутить страницу вниз на 100 пикселей"):
        web_driver.execute_script("window.scrollBy(0, 100);")

    with allure.step("Добавить товар 'Sauce Labs Bolt T-Shirt' в корзину"):
        shop_page.add_to_cart_by_product_id("add-to-cart-sauce-labs-bolt-t-shirt")

    with allure.step("Прокрутить страницу вниз на 400 пикселей"):
        web_driver.execute_script("window.scrollBy(0, 400);")

    with allure.step("Добавить товар 'Sauce Labs Onesie' в корзину"):
        shop_page.add_to_cart_by_product_id("add-to-cart-sauce-labs-onesie")

    with allure.step("Прокрутить страницу в верхнюю часть страницы"):
        web_driver.execute_script("window.scrollTo(0, 0)")

    with allure.step("Перейти в корзину"):
        shop_page.go_to_cart()

    cart_page = CartPage(web_driver)
    with allure.step("Перейти к оформлению заказа"):
        cart_page.click_checkout()

    checkout_page = CheckoutPage(web_driver)
    with allure.step("Заполнить данные клиента"):
        checkout_page.fill_customer_info("Имя", "Фамилия", "12345")

    with allure.step("Получить итоговую сумму заказа"):
        total_text = checkout_page.get_total()

    with allure.step(f"Проверить, что итоговая сумма содержит '$58.29' (фактическая: '{total_text}')"):
        assert "$58.29" in total_text, (
            f"Ожидалась сумма '$58.29' в тексте тотала, но было: '{total_text}'"
        )