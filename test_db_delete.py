import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

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


def test_delete_teacher(session):
    # Создаем тестового преподавателя с уникальным teacher_id
    test_teacher_id = 88888
    teacher = session.query(Teacher).filter_by(
        teacher_id=test_teacher_id).first()

    if not teacher:
        teacher = Teacher(
            teacher_id=test_teacher_id,
            email="test.teacher@example.com",
            group_id=1
        )
        session.add(teacher)
        session.commit()

    # Проверяем, что преподаватель есть в базе
    teacher_from_db = session.query(Teacher).filter_by(
        teacher_id=test_teacher_id).first()
    assert teacher_from_db is not None

    # Удаляем преподавателя
    session.delete(teacher_from_db)
    session.commit()

    # Проверяем, что преподаватель удалён
    deleted_teacher = session.query(Teacher).filter_by(
        teacher_id=test_teacher_id).first()
    assert deleted_teacher is None
