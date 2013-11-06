from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import config
import datetime

engine = create_engine(config.DB_URL, echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('sections.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.now)
    comment = Column(String(255))
    num_responses = Column(Integer)

    user = relationship("User", backref="comment")
    section = relationship("Section", backref="comment")

class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)
    html_section = Column(String(60))
    site_id = Column(ForeignKey('sites.id'))
    num_favorites = Column(Integer, default=0)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    github_name = Column(String(60))

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('sections.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True)
    url = Column(String(255))

def create_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()

