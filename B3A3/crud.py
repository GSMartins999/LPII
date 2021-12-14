from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from A3B3.models.models import Cadastro, Cliente, Compra, Editora, Livro
from models.models import Atividade, Comentario, Usuario

engine = create_engine("mysql+pymysql://root:@localhost/A3B3", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def create1():

    cliente1 = Cliente(nome='João', sobrenome='Silva', codigo='123')
    cadastro1 = Cadastro(endereco='VGA', telefone='2121-2121', cpf='11.111.111/0001-1', lista_de_livros='livro 1')
    cliente1.cadastro.append(cadastro1) 
    compra1 = Compra()
    cliente1.compra.append(compra1)
    session.add(cliente1)
    session.commit()
    
def create2(): 

    cliente2 = Cliente(nome='Aurora', sobrenome='Bonffin', codigo='1234')

    cadastro2 = Cadastro(endereco='VGA', telefone='2222-2222', cpf='22.222.222/0001-2', lista_de_livros='livro 2')
    cliente2.cadastro.append(cadastro2) 
    compra2 = Compra()
    cliente2.compra.append(compra2)
    session.add(cliente2)
    session.commit()

def create3():
    
    cliente3 = Cliente(nome='Jeferson', sobrenome='Gomes', codigo='12345')
    cadastro3 = Cadastro(endereco='VGA', telefone='2323-2323', cpf='33.333.333/0001-3', lista_de_livros='livro 3')
    cliente3.cadastro.append(cadastro3) 
    compra3 = Compra()
    cliente3.compra.append(compra3)
    session.add(cliente3)
    session.commit()

def create4():

    editora1 = Editora(nome='Pandora', codigo='123', telefone='3131-3131', gerente='')
    livro1 = Livro(titulo='Os três porquinhos', autor='José Bonifácio', assunto='drama/terror', ISBN='97512-0', quantidade='18')
    editora1.livro.append(livro1) 
    session.add(editora1)
    session.commit()

def create5():

    editora2 = Editora(nome='Rocco', codigo='1234', telefone='3232-3232', gerente='Pedro Lucas')
    livro2 = Livro(titulo='A bela e a fera', autor='João da esquina', assunto='Romance', ISBN='65342-0', quantidade='02')
    editora2.livro.append(livro2) 
    session.add(editora2)
    session.commit()

def create6():

    editora3 = Editora(nome='FTD', codigo='12345', telefone='3333-3333', gerente='Lorena Dantas')
    livro3 = Livro(titulo='Harry Potter', autor='J. K. Rowling', assunto='drama/ficção/ação', ISBN='85420-0', quantidade='05')
    editora3.livro.append(livro3) 
    session.add(editora3)  
    session.commit()
