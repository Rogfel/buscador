from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

dbPath = os.path.join(os.path.dirname(__file__), os.pardir , "db", "matrix.sqlite")
db_engine = create_engine('sqlite:///%s' % dbPath, echo=True)

__SessionClass = sessionmaker(bind = db_engine)
db_default_session = __SessionClass()