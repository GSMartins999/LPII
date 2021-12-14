from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from models.models import Atividade, Comentario, Usuario

engine = create_engine("mysql+pymysql://root:@localhost/A2B3", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create1():
    user1 = Usuario(email='joão@gmail.com', senha='123')

    atividade1 = Atividade(inicio='05-10-2021', fim='05-10-2021', quilometro='02,7', tipo='maratona', local='VGA')
    user1.atividade.append(atividade1) 

    atividade2 = Atividade(inicio='11-10-2021', fim='11-10-2021', quilometro='8,00', tipo='corrida', local='VGA')
    user1.atividade.append(atividade2)

    atividade3 = Atividade(inicio='10-11-2021', fim='11-11-2021', quilometro='6,00', tipo='corrida', local='VGA')
    user1.atividade.append(atividade3)

    comentario1 = Comentario(comentario='Desafiador')
    user1.comentario.append(comentario1)
    
    session.add(user1)
    session.commit()
    
def create2():
    user2 = Usuario(email='gabriel@gamil.com', senha='1234')

    atividade4 = Atividade(inicio='02-08-2021', fim='02-08-2021', quilometro='05,5', tipo='maratona', local='VGA')
    user2.atividade.append(atividade4) 

    atividade5 = Atividade(inicio='03-10-2021', fim='03-10-2021', quilometro='10,00', tipo='corrida', local='VGA')
    user2.atividade.append(atividade5)

    atividade6 = Atividade(inicio='10-12-2021', fim='10-12-2021', quilometro='06,2', tipo='corrida', local='VGA')
    user2.atividade.append(atividade6)

    comentario2 = Comentario(comentario='gostei')
    user2.comentario.append(comentario2)

    comentario3 = Comentario(comentario='podia ser melhor')
    user2.comentario.append(comentario3)

    session.add(user2)
    session.commit()

def create3():
    user3 = Usuario(email='daniel@gmail.com', senha='12345')

    atividade7 = Atividade(inicio='10-12-2021', fim='10-12-2021', quilometro='07,5', tipo='maratona', local='VGA')
    user3.atividade.append(atividade7) 

    atividade8 = Atividade(inicio='09-05-2021', fim='10-05-2021', quilometro='06,00', tipo='corrida', local='VGA')
    user3.atividade.append(atividade8)

    atividade9 = Atividade(inicio='05-02-2020', fim='05-02-2020', quilometro='09,00', tipo='corrida', local='VGA')
    user3.atividade.append(atividade9)

    comentario4 = Comentario(comentario='achei bem interessante')
    user3.comentario.append(comentario4)

    session.add(user3)
    session.commit()

def update():

    user = session.query(Usuario).filter(Usuario.id == 1).one()
    user.senha = "senhausu1"
    session.commit()

def delete():

    atividade = session.query(Atividade).get(2)
    session.delete(atividade)
    session.commit()