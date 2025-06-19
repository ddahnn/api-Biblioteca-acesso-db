from sqlalchemy.orm import Session  # type: ignore
from models.Livro import Livro
from schemas.livro_schema import LivroCreate




# cria o livro
def criar_livro(db: Session, livro:LivroCreate):
    db_livro = Livro(**livro.dict())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro


# Exibe todos os livros
def exibir_livros(db:Session):
    return db.query(Livro).all


#busca livro por PK ISBN 
def buscar_Por_isbn(db: Session , isbn:str):
    return db.query(Livro).filter(Livro.isbn == isbn).first()

# Excluir livro
def Excluir_Livro(db: Session, isbn: str):
    db_livro = db.query(Livro).filter(Livro.isbn == isbn).first()
    if db_livro:
        db.delete(db_livro)
        db.commit()
        return True
    return False