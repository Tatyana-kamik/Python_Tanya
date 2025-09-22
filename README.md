# Python_Tanya
# Автоматизация тестирования медленного калькулятора

Данный проект содержит автоматизированные тесты для проверки работы медленного калькулятора на сайте [https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html).

## Структура проекта

- **calculator_page.py** — описание Page Object для страницы калькулятора.
- **test_calculator.py** — автотесты, использующие Page Object.
- **README.md** — документация по проекту.

## Установка и подготовка

1. Установите Python 3.6+.
2. Установите зависимости:
bash
pip install selenium pytest allure-pytest

3. Скачайте ChromeDriver, подходящий под вашу версию Google Chrome, и добавьте его в PATH.

## Запуск тестов

Для запуска тестов и формирования Allure отчёта выполните:
bash
pytest --alluredir=allure-results

где `allure-results` — папка для сохранения файлов отчёта.

## Просмотр отчёта

1. Убедитесь, что установлен Allure Commandline:

- Для Windows: скачайте с https://github.com/allure-framework/allure2/releases
- Для Linux/macOS: установите через пакетный менеджер или с помощью scoop/brew.

2. Запустите локальный сервер просмотра отчёта следующей командой:
bash
allure serve allure-results

После этого в браузере откроется страница с подробным отчётом о выполнении тестов. 

# Автоматизированное тестирование сайта SauceDemo

В проекте реализован автоматизированный тест оформления заказа на сайте [https://www.saucedemo.com/](https://www.saucedemo.com/) с использованием паттерна Page Object Model.

## Структура проекта

- **shopmag_page.py** — классы страниц (LoginPage, ShopPage, CartPage, CheckoutPage).
- **test_shopmag.py** — автотесты с применением Page Object.
- **README.md** — документация.

## Установка и настройка

1. Убедитесь, что установлен Python 3.6+.
2. Установите зависимости:
bash
pip install selenium pytest allure-pytest webdriver-manager

3. Для запуска тестов используется Firefox. Убедитесь, что установлен Firefox.

## Запуск тестов

Запустите тесты и сохраните результаты для Allure:
bash
pytest --alluredir=allure-results

## Просмотр Allure отчёта

1. Установите Allure commandline:

- Windows: скачайте с https://github.com/allure-framework/allure2/releases
- Linux/macOS: установите через пакетный менеджер (brew, apt, etc.).

2. Запустите локальный сервер с отчётом командой:
bash
allure serve allure-results

Откроется браузер с красивым интерактивным отчётом.