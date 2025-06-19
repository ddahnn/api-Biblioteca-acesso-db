from sqlalchemy import Column, String, Integer, ForeignKey # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from config.database import Base


class Livro(Base):
    __tablename__ = 'livros'

    isbn = Column(String(13), primary_key = True, index=True)
    nome= Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    editora = Column(String(50), nullable=False)
    id_autor = Column(Integer, ForeignKey('autores.id'), nullable = False)

autor = relationship("Autor")