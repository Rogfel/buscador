# -*- coding=utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import Float
from sqlalchemy import ForeignKey

import os
from sqlalchemy import create_engine

Base = declarative_base()
dbPath = os.path.join(os.path.dirname(__file__), os.pardir , "db", "matrix.sqlite")
db_engine = create_engine('sqlite:///%s' % dbPath, echo=True)

class BaseMatrix(Base):
    __tablename__ = 'matrix'
    id = Column(Integer, Sequence('matrix_id'), primary_key=True)
    last_update = Column(String(10))
    matrix = Column(String())


    def __init__(self ):
        pass

if __name__ == '__main__':
    Base.metadata.create_all(db_engine)