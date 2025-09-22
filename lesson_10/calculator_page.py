from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """
    Класс, представляющий страницу калькулятора.
    Обеспечивает взаимодействие с элементами страницы для автоматизированного тестирования.
    """

    def __init__(self, driver):
        """
        Инициализация экземпляра класса CalculatorPage.

        :param driver: WebDriver - объект драйвера Selenium для управления браузером.
        :return: None
        """
        self.driver = driver
        # Локаторы элементов страницы
        self.DELAY_INPUT = (By.CSS_SELECTOR, '#delay')
        self.DISPLAY = (By.CSS_SELECTOR, '#calculator .screen')

    def open(self, url: str) -> None:
        """
        Открыть заданную страницу в браузере.

        :param url: str - URL страницы для открытия.
        :return: None
        """
        self.driver.get(url)

    def scroll_down(self, offset_y: int = 300) -> None:
        """
        Прокрутить страницу вниз на заданное количество пикселей.

        :param offset_y: int - величина прокрутки по вертикали (по умолчанию 300).
        :return: None
        """
        self.driver.execute_script(f"window.scrollBy(0, {offset_y});")

    def set_delay(self, value: str, timeout: int = 20) -> None:
        """
        Ввести значение задержки в соответствующее поле.

        :param value: str - значение задержки для ввода.
        :param timeout: int - максимальное время ожидания появления поля (секунды).
        :return: None
        """
        delay_el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_el.clear()
        delay_el.send_keys(value)

    def _click_by_text(self, text: str, timeout: int = 20) -> None:
        """
        Внутренний метод для клика по кнопке с заданным текстом.

        :param text: str - текст кнопки для клика.
        :param timeout: int - максимальное время ожидания кликабельности кнопки (секунды).
        :return: None
        """
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']"))
        ).click()

    def click_digit(self, digit: str) -> None:
        """
        Нажать кнопку с цифрой.

        :param digit: str - цифра для нажатия (от '0' до '9').
        :return: None
        """
        self._click_by_text(digit)

    def click_operator(self, operator: str) -> None:
        """
        Нажать кнопку с арифметическим оператором.

        :param operator: str - оператор для нажатия ('+', '-', '*', '/', и т.д.).
        :return: None
        """
        self._click_by_text(operator)

    def click_equals(self) -> None:
        """
        Нажать кнопку равенства '='.

        :return: None
        """
        self._click_by_text('=')

    def get_result(self, timeout: int = 20) -> str:
        """
        Получить текущий результат из экрана калькулятора.

        :param timeout: int - максимальное время ожидания появления результата (секунды).
        :return: str - текст результата.
        """
        display_el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.DISPLAY)
        )
        return display_el.text