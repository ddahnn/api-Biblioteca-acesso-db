from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from schemas.usuario_schema import Usuario, UsuarioCreate
from services import usuario_services
from typing import List


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

# Dependência para conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Criar usuário
@router.post("/", response_model=Usuario)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_services.criar_usuario(db, usuario)


# Listar todos os usuários
@router.get("/", response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()


# Buscar usuário por username (login)
@router.get("/buscar/{username}", response_model=Usuario)
def buscar_usuario(username: str, db: Session = Depends(get_db)):
    db_usuario = usuario_services.buscar_Username(db, username)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario


# Deletar usuário
@router.delete("/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    sucesso = usuario_services.deletar_usuario(db, usuario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"mensagem": "Usuário deletado com sucesso"}
