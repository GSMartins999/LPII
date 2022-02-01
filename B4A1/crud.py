from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from B4A1.models.models import Cadastro, Cliente, Compra, Produtora, Dvd

engine = create_engine("mysql+pymysql://root:@localhost/B4A1", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def create1(): 

    cliente1 = Cliente(nome='Hellen', sobrenome='Nascimento', codigo='1234')

    cadastro1 = Cadastro(endereco='SP', telefone='1111-1111', cpf='11.111.111/0001-1', lista_de_filmes='dvd 1')
    cliente1.cadastro.append(cadastro1) 
    compra1 = Compra()
    cliente1.compra.append(compra1)
    session.add(cliente1)
    session.commit()
    
def create2(): 

    cliente2 = Cliente(nome='Gorete', sobrenome='Nani', codigo='1234')

    cadastro2 = Cadastro(endereco='VGA', telefone='2222-2222', cpf='22.222.222/0001-2', lista_de_filmes='dvd 2')
    cliente2.cadastro.append(cadastro2) 
    compra2 = Compra()
    cliente2.compra.append(compra2)
    session.add(cliente2)
    session.commit()

def create3():
    
    cliente3 = Cliente(nome='Jeferson', sobrenome='Gomes', codigo='12345')
    cadastro3 = Cadastro(endereco='VGA', telefone='2323-2323', cpf='33.333.333/0001-3', lista_de_filmes='dvd 3')
    cliente3.cadastro.append(cadastro3) 
    compra3 = Compra()
    cliente3.compra.append(compra3)
    session.add(cliente3)
    session.commit()

def create4():

    produtora1 = Produtora(nome='Kleiton', codigo='123', telefone='3131-3131', gerente='João')
    dvd1 = Dvd(titulo='Os três porquinhos', autor='José Bonifácio', assunto='drama/terror', ISBN='97512-0', quantidade='18')
    produtora1.dvd.append(dvd1) 
    session.add(produtora1)
    session.commit()

def create5():

    produtora2 = Produtora(nome='Disney', codigo='1234', telefone='3232-3232', gerente='Hellenildo Santos')
    dvd2 = Dvd(titulo='A bela e a fera', autor='João da esquina', assunto='Romance', ISBN='65342-0', quantidade='02')
    produtora2.dvd.append(dvd2) 
    session.add(produtora2)
    session.commit()

def create6():

    produtora3 = Produtora(nome='Paramount', codigo='12345', telefone='3333-3333', gerente='Lucas Dantas')
    dvd3 = Dvd(titulo='Harry Potter', autor='J. K. Rowling', assunto='drama/ficção/ação', ISBN='85420-0', quantidade='05')
    produtora3.dvd.append(dvd3) 
    session.add(produtora3)  
    session.commit()