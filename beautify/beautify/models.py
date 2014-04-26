from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Python(Base):
    __tablename__ = 'python'

    url = Column(Text, primary_key=True)
    title = Column(Text),
    summary = Column(Text)

class Ruby(Base):

    __tablename__ = 'ruby'

    url = Column(Text, primary_key=True)
    title = Column(Text),
    summary = Column(Text)

class PHP(Base):
    __tablename__ = 'php'

    url = Column(Text, primary_key=True)
    title = Column(Text),
    summary = Column(Text)

class C(Base):
    __tablename__ = 'c'

    url = Column(Text, primary_key=True)
    title = Column(Text),
    summary = Column(Text)

class JavaScript(Base):

    __tablename__ = 'javascript'

    url = Column(Text, primary_key=True)
    title = Column(Text),
    summary = Column(Text)

class CPP(Base):
    __tablename__ = 'cpp'

    url = Column(Text, primary_key=True)
    title = Column(Text),
    summary = Column(Text)

class ObjectiveC(Base):
    __tablename__ = "objectivec"

    url = Column(Text, primary_key=True)
    title = Column(Text),
    summary = Column(Text)
