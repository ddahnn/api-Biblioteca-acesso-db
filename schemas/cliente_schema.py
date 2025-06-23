from pydantic import BaseModel  # type: ignore


class ClienteBase(BaseModel):
    nome:str
    telefone:str

class ClienteCreate(ClienteBase):
    matricula:str

class Cliente(ClienteBase):
    matricula : str

    class Config:
        from_attributes = True
