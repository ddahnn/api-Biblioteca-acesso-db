from sqlalchemy import Column, Integer, String # type: ignore
from config.database import Base



class Autor(Base):
    __tablename__ = 'autores'


    id = Column(Integer,primary_key = True , index=True)
    nome = Column(String(30), nullable=False)
    pais_origem = Column(String(30),nullable=False)