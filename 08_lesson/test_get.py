import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2/projects"
HEADERS = {
    "Authorization": ""
    "Bearer RPzVlsAUBXy3HyfCEBbWq+iesg1EBW1PvMY4QTJ3Z4ZZtOTPVzks76p4Ge6FooEZ",
    "Content-Type": "application/json"
}


@pytest.fixture
def create_project():
    project_data = {"title": "SkyPro project"}
    response = requests.post(BASE_URL, headers=HEADERS, json=project_data)
    response.raise_for_status()  # Если ошибка, будет выброшено исключение
    return response.json()["id"]


def test_get_project_positive(create_project):
    project_id = create_project  # Получение ID существующего проекта
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)

    assert response.status_code == 200  # Ожидаем статус 200 OK
    response_data = response.json()
    assert "id" in response_data  # Проверяем, что в ответе есть ID
    assert response_data["id"] == project_id  # Проверяем, что ID совпадает


def test_get_project_negative():
    nonexistent_id = "999999999"  # Используем ID, который точно не существует
    response = requests.get(f"{BASE_URL}/{nonexistent_id}", headers=HEADERS)

    assert response.status_code == 404  # Ожидаем статус 404 Not Found
    assert "message" in response.json()  # Проверяем наличие ошибки
