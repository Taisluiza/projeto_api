from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
import models
import schemas
from database import SessionLocal, engine

# Cria as tabelas no banco, caso não existam
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- ROTAS ----------------

# 1️⃣ Rota para criar estudante
# ALTERAÇÃO: troquei response_model=schemas.Estudante -> schemas.EstudanteResponse
@app.post('/estudantes/', response_model=schemas.EstudanteResponse)
def criar_estudante(
    estudante: schemas.EstudanteCreate,
    db: Session = Depends(get_db)
):
    db_estudante = models.Estudante(
        nome=estudante.nome,
        email=estudante.email,  # ALTERAÇÃO: incluir email
        perfil=models.Perfil(**estudante.perfil.dict())
    )
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante

# 2️⃣ Rota para listar estudantes
# ALTERAÇÃO: troquei response_model=List[schemas.Estudante] -> List[schemas.EstudanteResponse]
@app.get('/estudantes/', response_model=List[schemas.EstudanteResponse])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil)
    ).all()
    return estudantes
