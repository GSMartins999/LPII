from sqlalchemy import *
from models.models import Usuario, Atividade, Comentario, Curtida

<<<<<<< HEAD
engine = create_engine("mysql+pymysql://root:@localhost/B3A1", echo=True)
=======
engine = create_engine("mysql+pymysql://root:@localhost/B3A2", echo=True)
>>>>>>> 5cff2cbf859dc63bb47f51c924a902fa2bb1e872

usuario = Usuario.__table__
usuario.create(engine, checkfirst=True)

atividade = Atividade.__table__
atividade.create(engine, checkfirst=True)

curtida = Curtida.__table__
curtida.create(engine, checkfirst=True)

comentario = Comentario.__table__
<<<<<<< HEAD
comentario.create(engine, checkfirst=True)
=======
comentario.create(engine, checkfirst=True)

   
>>>>>>> 5cff2cbf859dc63bb47f51c924a902fa2bb1e872
