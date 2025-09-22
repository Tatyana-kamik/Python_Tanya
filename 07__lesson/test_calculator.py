import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page import CalculatorPage


@pytest.fixture
def web_driver():
    # Настройка для Chrome
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_slow_calculator_with_pom(web_driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    calc_page = CalculatorPage(web_driver)
    calc_page.open(url)

    # Прокрутка страницы, чтобы элементы были в области видимости
    calc_page.scroll_down()

    # Ввод значения 45 в поле задержки
    calc_page.set_delay('45')

    # Нажать кнопки 7, +, 8, =
    calc_page.click_digit('7')
    calc_page.click_operator('+')
    calc_page.click_digit('8')
    calc_page.click_equals()

    # Получить результат и проверить его
    result = calc_page.get_result()
    assert result == '15', f"Expected 15 but got {result}"
