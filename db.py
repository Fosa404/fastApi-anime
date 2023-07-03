from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:regimiento774@localhost:5432/anime')

Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()



def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()



