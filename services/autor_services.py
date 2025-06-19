from sqlalchemy.orm import Session # type: ignore
from models.Autor import Autor
from schemas.autor_schema import AutorCreate


#Cria  o Autor
def criar_Autor(db :Session, autor: AutorCreate):
    db_autor = Autor(**autor.dict())
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor



#  Lista todos os autores cadastrados
def listar_autores(db:Session):
    return db.query(Autor).all()



# Busca Autor por ID 
def buscar_autor_por_id(db: Session, autor_id: int):
    return db.query(Autor).filter(Autor.id == autor_id).first()




# Deletar Autor
def deletar_autor(db: Session, autor_id: int):
    db_autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if db_autor:
        db.delete(db_autor)
        db.commit()
        return True
    return False