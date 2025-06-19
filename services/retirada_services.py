from sqlalchemy.orm import Session   # type: ignore
from models.Retirada import Retirada
from models.Livro import Livro
from models.Cliente import Cliente
from schemas.retirada_schema import RetiradaCreate
from datetime import datetime, timedelta
from typing import Optional



# Função auxiliar para converter data string DD/MM/YYYY em objeto datetime
def converter_data(data_str: str) -> datetime:
    return datetime.strptime(data_str, "%d/%m/%Y")


# Criar retirada
def criar_retirada(db: Session, retirada: RetiradaCreate):
    cliente = db.query(Cliente).filter(Cliente.matricula == retirada.matricula_cliente).first()
    if not cliente:
        raise Exception("Cliente não encontrado.")
    livro = db.query(Livro).filter(Livro.isbn == retirada.isbn_livro).first()
    if not livro:
        raise Exception("Livro não encontrado.")
    livro_emprestado = db.query(Retirada).filter(
        Retirada.isbn_livro == retirada.isbn_livro,
        Retirada.status == "Retirado"
    ).first()
    if livro_emprestado:
        raise Exception("Livro não disponível para retirada.")
    retiradas_cliente = db.query(Retirada).filter(
        Retirada.matricula_cliente == retirada.matricula_cliente,
        Retirada.status == "Retirado"
    ).count()
    if retiradas_cliente >= 3:
        raise Exception("Cliente já possui 3 livros retirados. Devolva antes de retirar mais.")
    data_retirada = converter_data(retirada.data_retirada)
    data_prevista = data_retirada + timedelta(days=7)  # Aqui definimos o prazo de 7 dias
    db_retirada = Retirada(
        matricula_cliente=retirada.matricula_cliente,
        isbn_livro=retirada.isbn_livro,
        data_retirada=data_retirada,
        data_prevista=data_prevista,
        status="Retirado"
    )
    db.add(db_retirada)
    db.commit()
    db.refresh(db_retirada)
    return db_retirada


# Listar todas as retiradas
def listar_retiradas(db: Session):
    return db.query(Retirada).all()


# Buscar retirada por ID
def buscar_retirada_por_id(db: Session, retirada_id: int):
    return db.query(Retirada).filter(Retirada.id == retirada_id).first()


# Registrar devolução
def registrar_devolucao(db: Session, retirada_id: int, data_devolucao_str: str) -> Optional[int]:
    retirada = db.query(Retirada).filter(Retirada.id == retirada_id).first()
    if not retirada:
        raise Exception("Retirada não encontrada.")
    if retirada.status == "Devolvido":
        raise Exception("Este livro já foi devolvido.")
    data_devolucao = converter_data(data_devolucao_str)
    retirada.data_devolucao = data_devolucao
    retirada.status = "Devolvido"
    atraso = (data_devolucao - retirada.data_prevista).days
    dias_atraso = atraso if atraso > 0 else 0

    db.commit()
    db.refresh(retirada)

    return dias_atraso


# Deletar retirada (opcional, mais administrativo)
def deletar_retirada(db: Session, retirada_id: int):
    retirada = db.query(Retirada).filter(Retirada.id == retirada_id).first()
    if retirada:
        db.delete(retirada)
        db.commit()
        return True
    return False