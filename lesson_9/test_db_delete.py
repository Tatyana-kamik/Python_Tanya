import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

db = "postgresql://postgres:123@localhost:5432/QA"

engine = create_engine(db)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    email = Column(String)
    group_id = Column(Integer)


@pytest.fixture(scope="function")
def session():
    session = Session()
    yield session
    session.rollback()
    session.close()


def test_delete_teacher_with_sql(session):
    test_id = 88888

    # 1. Добавляем запись через INSERT
    insert_sql = text(
        "INSERT INTO teacher(teacher_id,email,group_id) VALUES (:id,:email,:group_id)"
        )
    session.execute(
        insert_sql, {
            'id': test_id, 'email': 'test@example.com', 'group_id': 1})
    session.commit()

    # 2. Проверяем добавление через SELECT
    select_sql = text("SELECT * FROM teacher WHERE teacher_id = :id")
    result = session.execute(select_sql, {'id': test_id})
    assert result.fetchone() is not None

    # 3. Удаляем через DELETE
    delete_sql = text("DELETE FROM teacher WHERE teacher_id = :id")
    session.execute(delete_sql, {'id': test_id})
    session.commit()

    # 4. Проверяем удаление
    result_after_delete = session.execute(select_sql, {'id': test_id})
    assert result_after_delete.fetchone() is None
