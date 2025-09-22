import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Настройки подключения к базе данных
db = "postgresql://postgres:123@localhost:5432/QA"

# Создание подключения к базе данных
engine = create_engine(db)
Session = sessionmaker(bind=engine)


@pytest.fixture(scope="function")
def session():
    # Создание новой сессии перед каждым тестом
    session = Session()
    yield session
    session.rollback()
    session.close()


def test_update_user_id(session):
    original_user_id = 99999
    updated_user_id = 99998

    session.execute(
        text(
            "INSERT INTO student (user_id, level, education_form, subject_id) "
            "SELECT:user_id,:level,:education_form,:subject_id "
            "WHERE NOT EXISTS (SELECT 1 FROM student WHERE user_id = :user_id)"
            ),
        {
            'user_id': original_user_id, 'level': 'Bachelor', 'education_form': 'Full-time', 'subject_id': 1
            }
    )
    session.commit()

    # Удаляем запись с updated_user_id
    session.execute(
        text("DELETE FROM student WHERE user_id = :user_id"),
        {'user_id': updated_user_id}
    )
    session.commit()

    # Обновляем user_id с помощью text()
    session.execute(
        text("UPDATE student SET user_id = :new_id WHERE user_id = :old_id"),
        {'new_id': updated_user_id, 'old_id': original_user_id}
    )
    session.commit()

    # Проверяем, что обновилось
    updated_student = session.execute(
        text("SELECT * FROM student WHERE user_id = :user_id"),
        {'user_id': updated_user_id}
    ).fetchone()  # Извлекаем первую запись

    assert updated_student is not None  # Проверяем, что запись существует
    assert updated_student.user_id == updated_user_id

    #удаляем тестовые данные
    session.execute(
        text("DELETE FROM student WHERE user_id = :user_id"),
        {'user_id': updated_user_id}
    )
    session.commit()  # Коммит после удаления
