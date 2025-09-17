from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def click_blue_button():
    # Настройка опций Chrome для подавления логов
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])

    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/dynamicid")

        # Ожидание и клик по синей кнопке (используем CSS-селектор)
        blue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )
        blue_button.click()

        print("Успешно кликнули на синюю кнопку")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    click_blue_button()
