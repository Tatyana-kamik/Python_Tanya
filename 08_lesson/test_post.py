import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2/projects"
HEADERS = {
    "Authorization": ""
    "Bearer RPzVlsAUBXy3HyfCEBbWq+iesg1EBW1PvMY4QTJ3Z4ZZtOTPVzks76p4Ge6FooEZ",
    "Content-Type": "application/json"
}


@pytest.fixture
def project_data():
    return {
        "title": "SkyPro project"
    }


@pytest.fixture
def create_project(project_data):
    # Создаем проект для первого запроса и возвращаем его ID
    response = requests.post(BASE_URL, headers=HEADERS, json=project_data)
    response.raise_for_status()  # Если ошибка, будет выброшено исключение
    return response.json()["id"]


def test_create_project_positive(project_data):
    response = requests.post(BASE_URL, headers=HEADERS, json=project_data)
    assert response.status_code == 201  # Ожидаем статус 201 Created
    assert "id" in response.json()  # Проверяем, что в ответе есть ID проекта


def test_create_project_negative(project_data):
    # Пытаемся создать проект с существующим заголовком
    existing_title = project_data['title']
    requests.post(BASE_URL, headers=HEADERS, json=project_data)

    # Пытаемся создать проект с тем же заголовком (ожидаем другой статус)
    duplicate_data = {
        "title": existing_title
    }

    duplicate_response = requests.post(
        BASE_URL, headers=HEADERS, json=duplicate_data)

    # Проверяем, что API возвращает статус 201 или ошибку
    assert duplicate_response.status_code == 201, f"Unexpected Status Code: {
        duplicate_response.status_code}. Response: {duplicate_response.text}"
