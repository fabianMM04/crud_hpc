import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Herramienta, Base

engine = create_engine('sqlite:///lista_herramienta.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


a= os.path.basename('/Applications/Calculator.app')
b= os.path.basename('/Applications/Android\ Studio.app')
c= os.path.basename('/Applications/Brackets.app')
d= os.path.basename('/Applications/Android\ Studio.app')
e= os.path.basename('/Applications/CodeBlocks.app')
f= os.path.basename('/Applications/Docker.app')
g= os.path.basename('/Applications/MATLAB_R2014b.app')
h= os.path.basename('/Applications/MySQLWorkbench.app')
i= os.path.basename('/Applications/Brackets.app')
j= os.path.basename('/Applications/PhpStorm.app')
k= os.path.basename('/Applications/PyCharm\ CE.app')
l= os.path.basename('/Applications/Python\ 2.7')


menuItem1 = Herramienta(nombre= a, descripcion="Juicy grilled veggie patty with tomato mayo and lettuce",
                     parametros="$7.50")

session.add(menuItem1)
session.commit()


menuItem2 = Herramienta(nombre=b, descripcion="Juicy grilled veggie patty with tomato mayo and lettuce",
                     parametros="$7.50")

session.add(menuItem2)
session.commit()

menuItem3 = Herramienta(nombre=c, descripcion="Juicy grilled veggie patty with tomato mayo and lettuce",
                     parametros="$7.50")

session.add(menuItem3)
session.commit()

menuItem4 = Herramienta(nombre=d, descripcion="Juicy grilled veggie patty with tomato mayo and lettuce",
                     parametros="$7.50")

session.add(menuItem4)
session.commit()

menuItem5 = Herramienta(nombre=e, descripcion="Juicy grilled veggie patty with tomato mayo and lettuce",
                     parametros="$7.50")

session.add(menuItem5)
session.commit()


menuItem6 = Herramienta(nombre=f, descripcion="Juicy grilled veggie patty with tomato mayo and lettuce",
                     parametros="$7.50")

session.add(menuItem6)
session.commit()
menuItem7 = Herramienta(nombre=g, descripcion="Juicy grilled veggie patty with tomato mayo and lettuce",
                     parametros="$7.50")

session.add(menuItem7)
session.commit()

menuItem8 = Herramienta(nombre=h, descripcion="Juicy grilled veggie patty with tomato mayo and lettuce",
                     parametros="$7.50")

session.add(menuItem8)
session.commit()

menuItem9 = Herramienta(nombre=i, descripcion="Juicy grilled veggie patty with tomato mayo and lettuce",
                     parametros="$7.50")

session.add(menuItem9)
session.commit()




print "added menu items!"

 
