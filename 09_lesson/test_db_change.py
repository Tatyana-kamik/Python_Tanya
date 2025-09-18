import pytest
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, declarative_base

db = "postgresql://postgres:123@localhost:5432/QA"

engine = create_engine(db)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)


@pytest.fixture(scope="function")
def session():
    session = Session()
    yield session
    session.rollback()
    session.close()


def test_update_user_id(session):
    original_user_id = 99999
    updated_user_id = 99998

    # Создаём запись, если её нет
    student = session.query(Student).filter_by(
        user_id=original_user_id).first()
    if not student:
        student = Student(
            user_id=original_user_id,
            level="Bachelor",
            education_form="Full-time",
            subject_id=1
        )
        session.add(student)
        session.commit()

# Удаляем запись с updated_user_id, если есть, для предотвращения конфликтов
    existing = session.query(Student).filter_by(
        user_id=updated_user_id).first()
    if existing:
        session.delete(existing)
        session.commit()

    # Обновляем user_id с помощью text() для явного обозначения текстового SQL
    session.execute(
        text("UPDATE student SET user_id = :new_id WHERE user_id = :old_id"),
        {'new_id': updated_user_id, 'old_id': original_user_id}
    )
    session.commit()

    # Проверяем, что обновилось
    updated_student = session.query(Student).filter_by(
        user_id=updated_user_id).first()
    assert updated_student is not None
    assert updated_student.user_id == updated_user_id

    # Чистим - удаляем тестовые данные
    session.delete(updated_student)
    session.commit()
