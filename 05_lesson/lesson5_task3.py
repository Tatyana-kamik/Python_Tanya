from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def input_numbers():
    # Настройка опций Firefox
    firefox_options = Options()
    firefox_options.add_argument('--headless')

    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(options=firefox_options)

    try:
        # Переход на страницу
        driver.get("http://the-internet.herokuapp.com/inputs")

        # Находим поле ввода
        input_field = driver.find_element(
            By.CSS_SELECTOR, "input[type='number']")

        # Вводим число 999
        input_field.send_keys("999")
        print("Введено число 999")

        # Очищаем поле
        input_field.clear()
        print("Поле очищено")

        # Вводим число 1000
        input_field.send_keys("1000")
        print("Введено число 1000")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        # Закрытие браузера
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    input_numbers()
