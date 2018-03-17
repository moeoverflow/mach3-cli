import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import sessionmaker
import os


Base = declarative_base()


class Subtitle(Base):
    __tablename__ = "subtitle"
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    start = Column(Text)
    end = Column(Text)
    fileName = Column(Text)

    def __repr__(self):
        return '{0}(title={1})'.format(self.__class__.__name__, self.text)


def add_entries(list_of_index_results, usr_dir):
    if usr_dir[:-1] == "/":
        pass
    else:
        usr_dir = usr_dir + "/"

    try:
        os.remove(usr_dir + "index_mach3.db")
    except OSError:
        pass

    engine = create_engine('sqlite:///{}index_mach3.db'.format(usr_dir), echo=False)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    Base.metadata.create_all(engine)
    for result_list in list_of_index_results:
        for result in result_list:
            entry = Subtitle(text=result["text"], start=result["start"], end=result["end"], fileName=result["file"])
            session.add(entry)
    session.commit()
    session.close()
