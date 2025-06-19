from fastapi import APIRouter, Depends, HTTPException   # type: ignore
from sqlalchemy.orm import Session   # type: ignore
from config.database import SessionLocal
from schemas.autor_schema import Autor, AutorCreate
from services import autor_services
from typing import List

router = APIRouter(
    prefix="/autores",
    tags=["Autores"]
)

# 🔗 Dependência para conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar Autor
@router.post("/", response_model=Autor)
def criar_autor(autor: AutorCreate, db: Session = Depends(get_db)):
    return autor_services.criar_Autor(db, autor)


# Listar todos os Autores
@router.get("/", response_model=List[Autor])
def listar_autores(db: Session = Depends(get_db)):
    return autor_services.listar_autores(db)


# Buscar Autor por ID
@router.get("/{autor_id}", response_model=Autor)
def buscar_autor(autor_id: int, db: Session = Depends(get_db)):
    db_autor = autor_services.buscar_autor_por_id(db, autor_id)
    if not db_autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return db_autor


# Deletar Autor
@router.delete("/{autor_id}")
def deletar_autor(autor_id: int, db: Session = Depends(get_db)):
    sucesso = autor_services.deletar_autor(db, autor_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return {"mensagem": "Autor deletado com sucesso"}
