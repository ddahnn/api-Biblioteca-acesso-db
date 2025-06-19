from sqlalchemy.orm import Session  # type: ignore
from models.Cliente import Cliente
from schemas.cliente_schema import ClienteCreate

# Criar Cliente
def criar_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Listar todos os clientes
def listar_clientes(db: Session):
    return db.query(Cliente).all()

# Buscar cliente por matrícula
def buscar_cliente_por_matricula(db: Session, matricula: str):
    return db.query(Cliente).filter(Cliente.matricula == matricula).first()

# Deletar cliente
def deletar_cliente(db: Session, matricula: str):
    db_cliente = db.query(Cliente).filter(Cliente.matricula == matricula).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
        return True
    return False
