from sqlalchemy import Column, String # type: ignore
from config.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    matricula = Column(String(20), primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False)
