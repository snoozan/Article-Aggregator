from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, String

import settings

def db_connect():
    """
    connects engine to postgres database in settings
    """
    return create_engine(URL(**settings.DATABASE))

DeclarativeBase = declarative_base()

def create_url_table(engine):

    """
    creates the table and its metadata
    """
    DeclarativeBase.metadata.create_all(engine)

class URLs(DeclarativeBase):

    """
    table full of article urls
    """

    __tablename__ = "urls"

    url = Column(String, primary_key=True)
    title = Column(String)


