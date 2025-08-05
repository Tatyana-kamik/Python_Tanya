from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_and_get_message():
    # Настройка опций Firefox
    firefox_options = Options()
    firefox_options.add_argument('--headless')

    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(options=firefox_options)

    try:
        # Переход на страницу логина
        driver.get("http://the-internet.herokuapp.com/login")

        # Ввод username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        print("Введен username: tomsmith")

        # Ввод password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        print("Введен password: SuperSecretPassword!")

        # Нажатие кнопки Login
        login_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("Нажата кнопка Login")

        # Ожидание появления зеленой плашки и получение текста
        flash_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        message_text = flash_message.text.strip()
        print("Текст сообщения:", message_text)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        # Закрытие браузера
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    login_and_get_message()
