from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def click_blue_button():
    # Настройка опций Chrome для подавления логов
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')  # подавляем большинство логов
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])

    # Инициализация драйвера Chrome с опциями
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/classattr")

        # Ожидание появления кнопки (явное ожидание лучше time.sleep())
        wait = WebDriverWait(driver, 10)
        blue_button = wait.until(
            EC.element_to_be_clickable(
                (
                 By.XPATH, "//button[contains("
                 "concat('', @class,''),'btn-primary')]")
            )
        )

        # Клик по кнопке
        blue_button.click()

        # Ожидание алерта и его закрытие
        try:
            wait.until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("Алерт не появился")

    except NoSuchElementException:
        print("Не удалось найти синюю кнопку")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    click_blue_button()
