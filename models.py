from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):    
    __tablename__ = 'estudantes'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    age = Column(Integer)

    # relação com Matricula
    matriculas = relationship("Matricula", back_populates="estudante")


class Matricula(Base):
    __tablename__ = 'matriculas'
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('estudantes.id'))  # chave estrangeira correta
    nome_disciplina = Column(String(100), nullable=False)

    # relação com Estudante
    estudante = relationship("Estudante", back_populates="matriculas")
