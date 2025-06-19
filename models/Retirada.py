from sqlalchemy import Column, Integer, String, Date, ForeignKey # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from config.database import Base


class Retirada(Base):
    __tablename__ = 'retiradas'
    id = Column(Integer, primary_key = True, index = True)
    matricula_cliente = Column(String(20), ForeignKey("clientes.matricula"), nullable = False)
    isbn_livro = Column(String(13), ForeignKey("livros.isbn"), nullable=False)
    data_retirada = Column(Date, nullable=False)
    data_prevista = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=False)
    status = Column(String(20), nullable = False, default="Retirado")

    cliente = relationship('Cliente')
    livro = relationship('Livro')
