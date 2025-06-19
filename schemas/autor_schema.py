from pydantic import BaseModel # type: ignore


#validação basica
class AutorBase(BaseModel):
    nome:str
    pasi_origem = str


#para a criação com os mesmos campos que a classe pai
class AutorCreate(AutorBase):
    pass



#inclui o id
class Autor(AutorBase):
    id:int

    class Config:
        orm_mode = True   # permite que o SQLAlchemy converta os objetos em dicionário, funcionando perfeitamente com Pydantic.