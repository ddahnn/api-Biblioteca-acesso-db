from sqlalchemy.orm import Session # type: ignore
from models.Usuario import Usuario
from schemas.usuario_schema import UsuarioCreate
from passlib.context import CryptContext # type: ignore


# Criptografia da senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# cria o hash da senha
def gerar_hash_senha(senha:str):
    return pwd_context.hash(senha)


#verificar senha
def _verificar_senha(senha:str, hash:str):
    return pwd_context.verify(senha, hash)



# Cria o usuario e salva no banco
def criar_usuario(db: Session, usuario:UsuarioCreate):
    hash_senha = gerar_hash_senha(usuario.senha)
    db_usuario = Usuario(username=usuario.username, senha =hash_senha)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


#busca user (login)
def buscar_Username(db: Session, username:str ):
    return db.query(Usuario).filter(Usuario.username == username).first()


# Deletar usuário 
def deletar_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
        return True
    return False