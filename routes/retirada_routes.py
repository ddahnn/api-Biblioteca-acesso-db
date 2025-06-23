from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from schemas.retirada_schema import Retirada, RetiradaCreate
from services import retirada_services
from typing import List


router = APIRouter(
    prefix="/retiradas",
    tags=["Retiradas"]
)

# Dependência para conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Criar retirada
@router.post("/", response_model=Retirada)
def criar_retirada(retirada: RetiradaCreate, db: Session = Depends(get_db)):
    try:
        return retirada_services.criar_retirada(db, retirada)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# listar todas as retiradas
@router.get("/", response_model=List[Retirada])
def listar_retiradas(db: Session = Depends(get_db)):
    return retirada_services.listar_retiradas(db)


# Buscar retirada por ID
@router.get("/{retirada_id}", response_model=Retirada)
def buscar_retirada(retirada_id: int, db: Session = Depends(get_db)):
    db_retirada = retirada_services.buscar_retirada_por_id(db, retirada_id)
    if not db_retirada:
        raise HTTPException(status_code=404, detail="Retirada não encontrada")
    return db_retirada


# Registrar devolução
@router.put("/{retirada_id}/devolver")
def registrar_devolucao(retirada_id: int, data_devolucao: str, db: Session = Depends(get_db)):
    try:
        dias_atraso = retirada_services.registrar_devolucao(db, retirada_id, data_devolucao)
        return {"mensagem": "Devolução registrada com sucesso", "dias_de_atraso": dias_atraso}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Deletar retirada
@router.delete("/{retirada_id}")
def deletar_retirada(retirada_id: int, db: Session = Depends(get_db)):
    sucesso = retirada_services.deletar_retirada(db, retirada_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Retirada não encontrada")
    return {"mensagem": "Retirada deletada com sucesso"}
