from pydantic import BaseModel
from typing import Optional

# ---------------- PERFIL ----------------
# ANTES: Perfil já tinha id, idade, endereco e era usado em tudo
# DEPOIS: separei em Base, Create e Response
class PerfilBase(BaseModel):
    idade: int
    endereco: str

class PerfilCreate(PerfilBase):
    pass

class PerfilResponse(PerfilBase):
    id: int
    class Config:
        orm_mode = True   # ANTES: from_attributes = True

# ---------------- ESTUDANTE ----------------
# ANTES: EstudanteBase tinha id, nome, perfil
# DEPOIS: EstudanteBase só tem campos comuns (nome, email)
class EstudanteBase(BaseModel):
    nome: str
    email: str

class EstudanteCreate(EstudanteBase):
    perfil: PerfilCreate   # ANTES: herdava id também

class EstudanteResponse(EstudanteBase):
    id: int
    perfil: Optional[PerfilResponse] = None
    class Config:
        orm_mode = True   # ANTES: from_attributes = True

# ---------------- MATRÍCULA ----------------
# ANTES: MatriculaBase tinha estudante_id + nome_disciplina
# DEPOIS: MatriculaBase só tem nome_disciplina
class MatriculaBase(BaseModel):
    nome_disciplina: str

class MatriculaCreate(MatriculaBase):
    estudante_id: int   # ANTES: herdava direto de Base

class MatriculaResponse(MatriculaBase):
    id: int
    estudante_id: int
    class Config:
        orm_mode = True   # ANTES: from_attributes = True
