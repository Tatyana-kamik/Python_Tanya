from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

db = "postgresql://postgres:123@localhost:5432/QA"

engine = create_engine(db)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Subject(Base):
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String)

# Test for adding a subject


def test_add_subject():
    session = Session()
    subject = Subject(subject_id=100, subject_title="Mathematics")
    session.add(subject)
    session.commit()
    saved = session.query(Subject).filter_by(subject_id=100).first()
    assert saved.subject_title == "Mathematics"
    session.delete(saved)
    session.commit()
    session.close()
