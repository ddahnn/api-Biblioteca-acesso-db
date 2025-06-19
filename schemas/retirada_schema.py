from pydantic import BaseModel, validador   # type: ignore
from typing import Optional
from datetime import date, datetime


class RetiradaBase(BaseModel):
    matricula_cliente: str
    isbn_livro : str
    data_retirada:str
    data_prevista:str
    data_devolucao:Optional[str] = None
    status:str

    @validador("data_retirada", "data_prevista","data_devolicao", pre=True, always= True)
    def validar_datas(cls, val):
        if val is None:
            return None
        try:
            if isinstance(val, date):
                return val.strftime("%d/%m/%Y")
            if isinstance(val, str):
                try:
                    datetime.strptime(val, "%d/%m/%Y")
                    return val
                except ValueError:
                    data = datetime.strptime(val, "%Y-%m-%d")
                    return data.strftime("%d/%m/%Y")
        except Exception as e:
            raise ValueError(f"Formato de data invalido {val}. use DD/MM/YYYY")
        

class RetiradaCreate(RetiradaBase):
    pass


class Retirada(RetiradaBase):
    id:int

    class config:
        orm_mode = True