from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # 1. Переход на страницу
    driver.get("http://uitestingplayground.com/textinput")

    # 2. Ввод текста "SkyPro" в поле ввода
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear()
    input_field.send_keys("SkyPro")

    # 3. Нажатие на синюю кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # 4. Ожидание обновления текста кнопки и получение нового значения
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    updated_button = driver.find_element(By.ID, "updatingButton")
    button_text = updated_button.text

    # 5. Вывод текста кнопки в консоль
    print(button_text)  # "SkyPro"

finally:
    # Закрытие браузера
    driver.quit()
