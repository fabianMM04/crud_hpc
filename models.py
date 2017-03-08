import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Herramienta(Base):
    __tablename__ = 'herramienta'

    nombre = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(250))
    parametros = Column(String(250))


    #We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):

       return {
           'nombre'         : self.nombre,
           'descripcion'         : self.descripcion,
           'id'         : self.id,
           'parametros'         : self.parametros,
       }


engine = create_engine('sqlite:///lista_herramienta.db')


Base.metadata.create_all(engine)

 
