import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Настройка для Chrome
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_slow_calculator(driver):
    # Шаг 1: Открыть страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollBy(0, 300);")
    # Шаг 2: Ввести значение 45
    delay_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#delay'))
    )
    delay_input.clear()
    delay_input.send_keys('45')
    # Шаг 3: Нажать кнопки 7, +, 8, =
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
    ).click()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
    ).click()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
    ).click()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
    ).click()

    result_element = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.ID, "screen"), "15")
    )
    result = result_element.text

    # Проверка, что результат равен 15
    assert result == '15', f"Expected 15 but got {result}"
