from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждем, пока не загрузятся минимум 3 картинки
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(
            By.CSS_SELECTOR, "#image-container img")) >= 3
    )

    # Получаем все картинки
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    print(f"Найдено картинок: {len(images)}")

    # Выводим все src для отладки
    for i, img in enumerate(images):
        print(f"Картинка {i}: {img.get_attribute('src')}")

    # Берем src третьей картинки (индекс 2)
    third_image_src = images[2].get_attribute("src")
    print(f"Третья картинка: {third_image_src}")

finally:
    driver.quit()
