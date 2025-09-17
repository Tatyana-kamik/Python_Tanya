from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера (укажите свой путь к драйверу)
driver = webdriver.Chrome()

try:
    # 1. Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # 2. Нажатие на синюю кнопку
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    # 3. Ожидание появления зеленой плашки и получение текста
    green_banner = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    message = green_banner.text

    # 4. Вывод текста в консоль
    print(message)  # "Data loaded with AJAX get request."

finally:
    # Закрытие браузера
    driver.quit()
