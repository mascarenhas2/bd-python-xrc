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
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome",String)
    email = Column("email",String)
    senha = Column("senha",String)
    
    #Definindo atributos de classe.
    def __init__(self, nome: str, email: str, senha : str):
        self.nome = nome 
        self.email = email
        self.senha = senha

#Criando tabela no banco de dados.
Base.metadata.create_all(bind = MEU_BANCO)

# CRUD.
# Create - Insert - Salvar.
os.system("cls || clear")
print("Solicitando dados para o usuário. ")

inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu e-mail: ")
inserir_senha = input("Digite sua senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha = inserir_senha)

session.add(cliente)
session.commit()

#Read - select - Consulta
print("\n Exibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

print("\n Atualizando dados do usuário.")
email_cliente = input("Digite o email do cliente que será atualizado: ")

cliente = session.query(Cliente).filter_by(email=email_cliente).first()

if cliente:
    cliente.nome = input("Digite seu nome: ")
    cliente.email = input("Digite seu email: ")
    cliente.senha = input("Digite sua senha: ")

    session.commit()

else:
    print("Cliente não encontrado.")

print("\n Exibindo dados de todos os clientes. ")
lista_clientes = session.query(Cliente).all() #Consulta o banco de dados "query" esconde o select e seleciona a tabela que voê deseja

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}" )

print("\n Excluindo os dados de um cliente.")
email_cliente = input("Digite o e-mail do cliente que será excluído: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente {cliente.nome} excluido com sucesso!")

else:
    print("Cliente não encontrado.")

#R - Read - SELECT - Consulta

print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} -{cliente.nome} - {cliente.email} - {cliente.senha} ")


print("Consultando os dados de um cliente.")
email_cliente = input("Digite o e-mail do cliente")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

else: 
    print("Cliente não encontrado.")


session.close()

