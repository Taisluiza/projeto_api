from pydantic import BaseModel
from typing import List, Optional

class EstudanteBase(BaseModel):   
     id: int
     nome: str
     perfil: Optional[Perfil] = None

     class Config:
      from_attributes = True

class EstudanteCreate(EstudanteBase):
        nome: str
        email: str
        perfil: PerfilCreate

class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str
    class Config:
        from_attributes = True

class PerfilCreate(BaseModel):
    idade: int
    endereco: str

class EstudanteResponse(EstudanteBase):
    id: int
    class Config:  #Informa para biblioteca para ler os campus estudantes diretamente.
        from_attributes = True

class MatriculaBase(BaseModel):
    estudante_id: int
    nome_disciplina: str

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int

    class Config:
        from_attributes = True