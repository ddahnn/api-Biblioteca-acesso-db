from pydantic import BaseModel  # type: ignore

class UsuarioBase(BaseModel):
    username:str

class UsuarioCreate(UsuarioBase):
    senha:str

class Usuario(UsuarioBase):
    id : int

    class Config:
        from_attributes = True
