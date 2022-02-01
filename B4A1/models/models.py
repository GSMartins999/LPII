from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DECIMAL, DateTime

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nome = Column(String(255), unique=True, nullable=False)
    sobrenome = Column(String(45), nullable=False)
    codigo = Column(int(255), nullable=False)

    cadastro = relationship("Cadastro",backref='Cliente', lazy=True)
    compra = relationship("Compra",backref='Cliente', lazy=True)

    def __repr__(self):
        return f'Cliente {self.cliente}'


class Cadastro(Base):
    __tablename__ = 'cadastro'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    endereco = Column(String(255), unique=True, nullable=False)
    telefone = Column(String(255), unique=True, nullable=False)
    cpf = Column(String(255), unique=True, nullable=False)
    lista_de_filmes = Column(String(255), unique=True, nullable=False)

    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship("Cliente", backref="Cadastro")

    def __repr__(self):
        return f'Cadastro {self.cadastro}'

class Produtora(Base):
    __tablename__ = 'produtora'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nome = Column(String(255), unique=True, nullable=False)
    codigo = Column(String(255), unique=True, nullable=False)
    telefone = Column(String(45), nullable=False)
    gerente = Column(String(255), unique=True, nullable=False)

    produtora = relationship("dvd",backref='produtora', lazy=True)

    def __repr__(self):
        return f'Produtora {self.produtora}'

class Dvd(Base):
    __tablename__ = 'Dvd'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    titulo = Column(String(255), nullable=True)
    produtor = Column(String(255), nullable=True)
    assunto = Column(String(255), nullable=True)
    ISBN = Column(String(255), nullable=True)
    quantidade = Column(int(255), nullable=True)

    compra = relationship("Compra",backref='Dvd', lazy=True)

    def __repr__(self):
        return f'dvd {self.dvd}'

class Compra(Base):
    __tablename__ = 'compra'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship("Cliente", backref="Compra")

    dvd_id = Column(Integer, ForeignKey('dvd.id'))
    dvd = relationship("dvd", backref="Compra")

    def __repr__(self):
        return f'Compra {self.compra}'