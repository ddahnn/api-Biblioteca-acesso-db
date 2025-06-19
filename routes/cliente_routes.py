from fastapi import APIRouter, Depends, HTTPException  # type: ignore
from sqlalchemy.orm import Session # type: ignore
from config.database import SessionLocal
from schemas.cliente_schema import Cliente, ClienteCreate
from services import cliente_services
from typing import List

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

# 🔗 Dependência para conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Criar Cliente
@router.post("/", response_model=Cliente)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_services.criar_cliente(db, cliente)


# ✅ Listar todos os clientes
@router.get("/", response_model=List[Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    return cliente_services.listar_clientes(db)


# ✅ Buscar cliente por matrícula
@router.get("/{matricula}", response_model=Cliente)
def buscar_cliente(matricula: str, db: Session = Depends(get_db)):
    db_cliente = cliente_services.buscar_cliente_por_matricula(db, matricula)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return db_cliente


# ✅ Deletar cliente
@router.delete("/{matricula}")
def deletar_cliente(matricula: str, db: Session = Depends(get_db)):
    sucesso = cliente_services.deletar_cliente(db, matricula)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"mensagem": "Cliente deletado com sucesso"}
