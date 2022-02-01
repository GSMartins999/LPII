from sqlalchemy import *
from models.models import Cliente, Cadastro, Compra, Produtora, Dvd


engine = create_engine("mysql+pymysql://root:@localhost/B4A1", echo=True)

cliente = Cliente.__table__
cliente.create(engine, checkfirst=True)

cadastro = Cadastro.__table__
cadastro.create(engine, checkfirst=True)

produtora = Produtora.__table__
produtora.create(engine, checkfirst=True)

dvd = Dvd.__table__
dvd.create(engine, checkfirst=True)

compra = Compra.__table__
compra.create(engine, checkfirst=True)