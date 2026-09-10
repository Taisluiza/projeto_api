from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

#Para criar a tabela, caso não tenha
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#criando rotas para o estudantes
@app.post(
        '/estudantes/', 
        response_model=schemas.EstudanteResponse)
def create_student(student: schemas.EstudanteCreate, 
                   db: Session = Depends(get_db)):

    db_student = models.Estudante(**student.model_dump()) #variavel para salvar as informações vinda do navegador
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

#para ler a rota de estudantes
@app.get(
        '/estudantes/',
         response_model=List[schemas.EstudanteResponse])#Retorno vai ser uma lista
def read_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).all() #Variavel para retornar os estudantes
    return students