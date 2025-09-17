import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2/projects"
HEADERS = {
    "Authorization": ""
    "Bearer RPzVlsAUBXy3HyfCEBbWq+iesg1EBW1PvMY4QTJ3Z4ZZtOTPVzks76p4Ge6FooEZ",
    "Content-Type": "application/json"
}


@pytest.fixture(scope="module")
def create_project():
    # Создаем проект и возвращаем его id
    project_data = {"title": "SkyPro project"}
    response = requests.post(BASE_URL, headers=HEADERS, json=project_data)
    response.raise_for_status()  # Если ошибка, будет выброшено исключение
    return response.json()["id"]


def test_update_project_positive(create_project):
    project_id = create_project
    update_data = {"title": "Updated SkyPro project"}
    response = requests.put(
        f"{BASE_URL}/{project_id}", headers=HEADERS, json=update_data)

    assert response.status_code == 200  # Ожидаем успешный статус 200 OK
    response_data = response.json()

    # Проверяем, что возвращается ID
    assert 'id' in response_data
    # ID должен совпадать с обновленным проектом
    assert response_data['id'] == project_id

    # GET-запрос, чтобы проверить, действительно ли обновилось название проекта
    get_response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    get_response_data = get_response.json()
    assert get_response.status_code == 200  # Ожидаем успешный статус 200 OK
    # Проверяем название проекта
    assert get_response_data['title'] == update_data['title']


def test_update_nonexistent_project():
    # Используем гарантированно несуществующий ID
    nonexistent_id = "999999999"  # замените на ID, который точно не существует
    update_data = {"title": "Some title"}
    response = requests.put(
        f"{BASE_URL}/{nonexistent_id}", headers=HEADERS, json=update_data)
# Ожидаем статус 404 Not Found
    assert response.status_code == 404
