from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):    
    __tablename__ = 'estudantes'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String)
    age = Column(Integer)

    # relação com Matricula e relação com o perfil
    matriculas = relationship("Matricula", back_populates="estudante")

    perfil = relationship("Perfil",
        back_populates="estudante",
        uselist=False,
        cascade="all, delete-orphan"
    )

class Perfil(Base):
    __tablename__ = 'perfis'

    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)
    #criando relação com chave estrangeira
    estudante_id = Column(
        Integer,
        ForeignKey("estudantes.id"),
        unique=True
    )
    estudante = relationship("Estudante", back_populates='perfil')

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    matriculas = relationship(
        "Matricula",
        back_populates='disciplina',
        cascade="all, delete-orphan"
    )


class Matricula(Base):
    __tablename__ = 'matriculas'
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('estudantes.id'))  # chave estrangeira correta
    nome_disciplina = Column(String(100), nullable=False)

    # relação com Estudante
    estudante = relationship("Estudante", back_populates="matriculas")

class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    estudantes = relationship(
        "Estudante", 
        back_populates="professor",
        cascade="all, delete-orphan"
    )