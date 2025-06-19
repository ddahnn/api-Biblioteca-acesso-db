from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from config.database import SessionLocal
from schemas.livro_schema import Livro, LivroCreate
from services import livro_services
from typing import List

router = APIRouter(
    prefix="/livros",
    tags=["Livros"]
)

# 🔗 Dependência para conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar Livro
@router.post("/", response_model=Livro)
def criar_livro(livro: LivroCreate, db: Session = Depends(get_db)):
    return livro_services.criar_livro(db, livro)


# Listar todos os livros
@router.get("/", response_model=List[Livro])
def listar_livros(db: Session = Depends(get_db)):
    return livro_services.exibir_livros(db)


# Buscar livro por ISBN
@router.get("/{isbn}", response_model=Livro)
def buscar_livro(isbn: str, db: Session = Depends(get_db)):
    db_livro = livro_services.buscar_Por_isbn(db, isbn)
    if not db_livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return db_livro


# Deletar livro
@router.delete("/{isbn}")
def deletar_livro(isbn: str, db: Session = Depends(get_db)):
    sucesso = livro_services.Excluir_Livro(db, isbn)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return {"mensagem": "Livro deletado com sucesso"}
