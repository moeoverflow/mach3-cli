from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

engine = create_engine('sqlite:///index_mach3.db', echo=False)

Base = declarative_base(engine)

try:
    class Subtitle(Base):
        __tablename__ = "subtitle"
        __table_args__ = {"autoload": True}
except sqlalchemy.exc.NoSuchTableError:
    print("No index database found. Please index this directory first: $ mach3 -i")


def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def index_search(query_text):
    session = loadSession()
    counter = 0
    options = list()
    for subtitle in session.query(Subtitle).filter(Subtitle.text.ilike("%{}%".format(query_text))):
        counter += 1
        print(counter, "-  ", subtitle.text, " : ", subtitle.fileName.split("/")[-1][:-4])
        options.append({"text": subtitle.text, "start": subtitle.start, "end": subtitle.end, "file": subtitle.fileName})
    print("Found {} results.".format(counter))
    return options