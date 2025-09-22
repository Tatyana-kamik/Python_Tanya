import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page import CalculatorPage


@pytest.fixture
def web_driver():
    """
    Фикстура для инициализации и завершения работы веб-драйвера Chrome.
    :return: WebDriver - объект драйвера браузера Chrome.
    """
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@allure.title("Тест медленного калькулятора с использованием Page Object Model")
@allure.description("Проверка корректности работы калькулятора с задержкой, "
                    "включая ввод значений, операции сложения и получения результата.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator_with_pom(web_driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    calc_page = CalculatorPage(web_driver)

    with allure.step("Открыть страницу калькулятора"):
        calc_page.open(url)

    with allure.step("Прокрутить страницу вниз для видимости элементов"):
        calc_page.scroll_down()

    with allure.step("Установить задержку обработки равной 1"):
        calc_page.set_delay('1')

    with allure.step("Нажать кнопку 7"):
        calc_page.click_digit('7')

    with allure.step("Нажать оператор +"):
        calc_page.click_operator('+')

    with allure.step("Нажать кнопку 8"):
        calc_page.click_digit('8')

    with allure.step("Нажать кнопку = для получения результата"):
        calc_page.click_equals()

    with allure.step("Получить и проверить результат"):
        result = calc_page.get_result()
        with allure.step(f"Проверка, что результат равен 15, а не {result}"):
            assert result == '15', f"Expected 15 but got {result}"