from db import Base
from sqlalchemy import Column, Integer, String, Float
from db import engine


class Animes(Base):
    __tablename__ = 'top_animes'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    episodes = Column(Integer)
    ranking = Column(Integer)
    score = Column(Float(2))
    aired = Column(String)
    img = Column(String)


Base.metadata.create_all(engine)

