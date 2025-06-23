from pydantic import BaseModel # type: ignore


#validação basica
class AutorBase(BaseModel):
    nome:str
    pais_origem: str


#para a criação com os mesmos campos que a classe pai
class AutorCreate(AutorBase):
    pass



#inclui o id
class Autor(AutorBase):
    id:int
    
    class Config:
        from_attributes = True
