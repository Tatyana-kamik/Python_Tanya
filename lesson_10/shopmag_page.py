from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс для работы с страницей авторизации.
    Позволяет открыть страницу, ввести логин и пароль, выполнить вход.
    """

    def __init__(self, driver):
        """
        Инициализация экземпляра LoginPage.

        :param driver: WebDriver - объект драйвера Selenium.
        :return: None
        """
        self._driver = driver
        self._USERNAME_INPUT = (By.ID, "user-name")
        self._PASSWORD_INPUT = (By.ID, "password")
        self._LOGIN_BUTTON = (By.ID, "login-button")

    def open(self, url: str) -> None:
        """
        Открыть страницу авторизации.

        :param url: str - URL страницы для открытия.
        :return: None
        """
        self._driver.get(url)

    def input_username(self, username: str, timeout: int = 20) -> None:
        """
        Ввести имя пользователя в поле логина.

        :param username: str - имя пользователя.
        :param timeout: int - время ожидания поля (сек).
        :return: None
        """
        username_el = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(self._USERNAME_INPUT)
        )
        username_el.clear()
        username_el.send_keys(username)

    def input_password(self, password: str, timeout: int = 20) -> None:
        """
        Ввести пароль в поле пароля.

        :param password: str - пароль пользователя.
        :param timeout: int - время ожидания поля (сек).
        :return: None
        """
        password_el = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(self._PASSWORD_INPUT)
        )
        password_el.clear()
        password_el.send_keys(password)

    def click_login(self, timeout: int = 20) -> None:
        """
        Нажать кнопку входа (Login).

        :param timeout: int - время ожидания кнопки (сек).
        :return: None
        """
        login_btn = WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        )
        login_btn.click()


class ShopPage:
    """
    Класс для работы со страницей магазина.
    Позволяет добавлять товары в корзину и переходить к корзине.
    """

    def __init__(self, driver):
        """
        Инициализация экземпляра ShopPage.

        :param driver: WebDriver - объект драйвера Selenium.
        :return: None
        """
        self._driver = driver
        self._CART_LINK = (
            By.CSS_SELECTOR, "a.shopping_cart_link[data-test='shopping-cart-link']"
        )

    def add_to_cart_by_product_id(self, product_id: str, timeout: int = 20) -> None:
        """
        Добавить товар в корзину по его id (идентификатор кнопки "Add to cart").

        :param product_id: str - id кнопки товара (например, 'add-to-cart-sauce-labs-backpack').
        :param timeout: int - время ожидания кнопки (сек).
        :return: None
        """
        add_button_locator = (By.ID, product_id)
        add_btn = WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(add_button_locator)
        )
        add_btn.click()

    def go_to_cart(self, timeout: int = 20) -> None:
        """
        Перейти в корзину, нажав на ссылку корзины.

        :param timeout: int - время ожидания ссылки (сек).
        :return: None
        """
        cart_btn = WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(self._CART_LINK)
        )
        cart_btn.click()


class CartPage:
    """
    Класс для работы со страницей корзины.
    Позволяет перейти к оформлению заказа и получить содержимое корзины.
    """

    def __init__(self, driver):
        """
        Инициализация экземпляра CartPage.

        :param driver: WebDriver - объект драйвера Selenium.
        :return: None
        """
        self._driver = driver
        self._CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-test='checkout']")

    def click_checkout(self, timeout: int = 20) -> None:
        """
        Нажать кнопку «Оформить заказ» (Checkout).

        :param timeout: int - время ожидания кнопки (сек).
        :return: None
        """
        checkout_btn = WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(self._CHECKOUT_BUTTON)
        )
        checkout_btn.click()

    def get_cart_contents(self, timeout: int = 20) -> list[str]:
        """
        Получить список названий товаров, находящихся в корзине.

        :param timeout: int - время ожидания элементов (сек).
        :return: list[str] - список названий товаров.
        """
        items = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )
        return [item.text for item in items]


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа.
    Позволяет заполнить данные клиента и получить итоговую сумму.
    """

    def __init__(self, driver):
        """
        Инициализация экземпляра CheckoutPage.

        :param driver: WebDriver - объект драйвера Selenium.
        :return: None
        """
        self._driver = driver
        self._FIRST_NAME_INPUT = (By.ID, "first-name")
        self._LAST_NAME_INPUT = (By.ID, "last-name")
        self._POSTAL_CODE_INPUT = (By.ID, "postal-code")
        self._CONTINUE_BUTTON = (By.XPATH, "//input[@value='Continue']")
        self._TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_customer_info(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
        timeout: int = 20
    ) -> None:
        """
        Заполнить форму с данными клиента и перейти далее.

        :param first_name: str - имя клиента.
        :param last_name: str - фамилия клиента.
        :param postal_code: str - почтовый индекс клиента.
        :param timeout: int - время ожидания элементов (сек).
        :return: None
        """
        first_el = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(self._FIRST_NAME_INPUT)
        )
        first_el.clear()
        first_el.send_keys(first_name)

        last_el = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(self._LAST_NAME_INPUT)
        )
        last_el.clear()
        last_el.send_keys(last_name)

        postal_el = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(self._POSTAL_CODE_INPUT)
        )
        postal_el.clear()
        postal_el.send_keys(postal_code)

        continue_btn = WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(self._CONTINUE_BUTTON)
        )
        continue_btn.click()

    def get_total(self, timeout: int = 20) -> str:
        """
        Получить текст с итоговой суммой заказа.

        :param timeout: int - время ожидания элемента (сек).
        :return: str - текст, содержащий итоговую сумму.
        """
        total_el = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(self._TOTAL_LABEL)
        )
        return total_el.text