import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    # Установка параметров для Firefox
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_saucedemo_checkout(driver):
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Добавление товаров в корзину
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    button.click()
    driver.execute_script("window.scrollBy(0, 100);")
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
    button.click()
    driver.execute_script("window.scrollBy(0, 400);")
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
    button.click()
    driver.execute_script("window.scrollTo(0, 0)")
    # Переход в корзину
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR, "a.shopping_cart_link["
                "data-test='shopping-cart-link']"
                ))
        )
    button.click()
    driver.execute_script("window.scrollTo(0, 400)")
    # Переход к оформлению заказа
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-test='checkout']"))
        )
    button.click()

    # Заполнение формы
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Имя")
    driver.find_element(By.ID, "last-name").send_keys("Фамилия")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()

    # Получение итоговой стоимости
    total_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label"))
    )
    total_amount = total_label.text.split()[-1]  # Получаем итоговую сумму

    # Проверка итоговой суммы
    assert total_amount == "$58.29", f"Итоговая сумма $58.29, но была {
        total_amount}"
