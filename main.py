""" BANCO DE DADOS
    - SQL (LINGUAGEM DE CONSULTA ESTRUTURADA)
    - EXEMPLO:
        - SELECT * FROM CLIENTES;
        - IRA CONSULTAR O BD NA TABELA CLIENTES.

        - SGBD:
            - GERENCIAR PERMISSÕES DE ACESSO 
            -ADMNISTRADOR DE BANCO DE DAODS (DBA)
            - CRIAR CONSULTAR PERSONALIZADAS
            -SELECT NOME, SOBRENOME, N_CART FROM CLIENTES:
        - ORM: MAPEAMENTO OBJETO RELACIONAL
         - USAR A LINGUAGEM DE PROGRAMAÇÃO PARA
            MANIPULAR O BANCO DE DADOS.
        - INSTALANDO ORM PARA PYTHON:
            - pip install sqlalchemy

"""

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()


# Criando tabela.

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    #Definindo campos de tabela.
    id = Column("id","Integer", primary_key=True, autoincrement=True)
    nome = Column("nome",String)
    email = Column("email",String)
    senha = Column("senha",String)
    
    #Definindo atributos de classe.
    def __init__(self, nome: str, email: str, senha : str):
        self.nome = nome 
        self.email = email
        self.senha = senha

#Criando tabela no banco de dados.
Base.meta.data.create_all(bind = MEU_BANCO)