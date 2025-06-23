from sqlalchemy import Column, Integer, String # type: ignore
from config.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)