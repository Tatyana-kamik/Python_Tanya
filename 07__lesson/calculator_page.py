from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        # Локаторы
        self.DELAY_INPUT = (By.CSS_SELECTOR, '#delay')
        self.DISPLAY = (By.ID, 'screen')

    # Открыть заданную страницу
    def open(self, url: str):
        self.driver.get(url)

    # Прокрутка страницы вниз на заданный offset
    def scroll_down(self, offset_y: int = 300):
        self.driver.execute_script(f"window.scrollBy(0, {offset_y});")

    # Ввод задержки
    def set_delay(self, value: str, timeout: int = 20):
        delay_el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_el.clear()
        delay_el.send_keys(value)

    # Внутренний помощник для клика по кнопке по тексту на кнопке
    def _click_by_text(self, text: str, timeout: int = 20):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']"))
        ).click()

    # Нажать цифру
    def click_digit(self, digit: str):
        self._click_by_text(digit)

    # Нажать оператор (+, -, *, / и т.д.)
    def click_operator(self, operator: str):
        self._click_by_text(operator)

    # Нажать =
    def click_equals(self):
        self._click_by_text('=')

    # Получить текущий результат
    def get_result(self, timeout: int = 20) -> str:
        display_el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.DISPLAY)
        )
        return display_el.text
