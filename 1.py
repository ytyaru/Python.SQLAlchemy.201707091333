#!python3
#coding: utf-8
#http://docs.sqlalchemy.org/en/latest/core/tutorial.html
import sqlalchemy
#from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
class Db:
    def __init__(self):
        print(sqlalchemy.__version__)
        self.create_engine()
        self.create_tables()
    def create_engine(self): self.__engine = sqlalchemy.create_engine('sqlite:///' + '1.db'); return self.__engine
    def create_tables(self):
        self.__metadata = sqlalchemy.MetaData()
        self.__tables = {}
        self.__tables['Users'] = sqlalchemy.Table('Users', self.__metadata,
                sqlalchemy.Column('Id', sqlalchemy.Integer, primary_key=True),
                sqlalchemy.Column('Name', sqlalchemy.String))
        self.__tables['Addresses'] = sqlalchemy.Table('Addresses', self.__metadata,
                sqlalchemy.Column('Id', sqlalchemy.Integer, primary_key=True),
                sqlalchemy.Column('UserId', None, sqlalchemy.ForeignKey('Users.Id')),
                sqlalchemy.Column('MailAddress', sqlalchemy.String))
        self.__metadata.create_all(self.__engine)
        return self.__metadata
    @property
    def Tables(self): return self.__tables
    def Engine(self): return self.__engine

db = Db()
engine = db.create_engine()
metadata = db.create_tables()
print(dir(metadata))
for t in metadata.tables: print(type(t), t)
print(db.Tables['Users'].insert())
print(db.Tables['Addresses'].insert())
print(db.Tables['Users'].insert().values(Name='name0'))
print(db.Tables['Users'].insert().values(Name='name0').compile().params)

#conn = db.Engine.connect()
conn = engine.connect()
print(conn)
result = conn.execute(db.Tables['Users'].insert().values(Name='name0'))
print(result.inserted_primary_key)
print(result)
print(dir(result))
print(result.keys())
for k in result.keys(): print(k, result[k])
