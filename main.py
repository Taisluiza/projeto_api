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

# DISCIPLINAS

@app.post('/disciplinas/', response_model=schemas.Disciplina)
def criar_disciplina(
        disciplina: schemas.DisciplinaCreate,
        db: Session = Depends(get_db)
    ):
    db_disciplina = models.Disciplina(**disciplina.dict())
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina

@app.get('/disciplinas/', response_model=List[schemas.Disciplina])
def listar_disciplinas(db: Session = Depends(get_db)):
    return db.query(models.Disciplina).all()


# PROFESSORES

@app.post('/professores/', response_model=schemas.Professor)
def criar_professor(
        professor: schemas.ProfessorCreate,
        db: Session = Depends(get_db)
    ):
    db_professor = models.Professor(**professor.dict())
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

@app.get('/professores/', response_model=List[schemas.Professor])
def listar_professores(db: Session = Depends(get_db)):
    return db.query(models.Professor).all()


# MATRÍCULAS

@app.post('/matriculas/', response_model=schemas.Matricula)
def criar_matricula(
        matricula: schemas.MatriculaCreate,
        db: Session = Depends(get_db)
    ):
    db_matricula = models.Matricula(**matricula.dict())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@app.get('/matriculas/', response_model=List[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):
    return db.query(models.Matricula).all()