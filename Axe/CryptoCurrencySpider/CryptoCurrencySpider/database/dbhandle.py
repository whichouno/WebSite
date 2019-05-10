from sqlalchemy.orm import *
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from ..database import dbinit as DBI
import traceback

if not database_exists(DBI.CONNECTION_STRING):
    create_database(DBI.CONNECTION_STRING)

mysql_engine = create_engine(DBI.CONNECTION_STRING)
db_Session = sessionmaker(bind=mysql_engine)
session = db_Session()

def CreateTable():
    DBI.Base.metadata.create_all(mysql_engine)

def Insert(data):
    try:
        session.add(data)
        session.commit()
        return True,None
    except Exception as ex:
        session.rollback()
        return False,ex

def Update(data):
    try:
        session.merge(data)
        session.commit()
    except:
        session.rollback()

def QueryOne():
    pass

def test():
    try:
        pass
    except:
        filepath = "/Users/ouno/Projects/python/cryptocurrency/error_log/err.txt"
        with open(filepath, 'a+') as fp:
            traceback.print_exc(file=fp)


CreateTable()
