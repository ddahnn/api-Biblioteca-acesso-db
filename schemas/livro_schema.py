from pydantic import BaseModel # type: ignore

class LivroBase(BaseModel):
    nome: str
    ano: int
    editora: str
    id_autor: int

class LivroCreate(LivroBase):
    isbn: str

class Livro(LivroBase):
    isbn: str

    class Config:
        from_attributes = True
