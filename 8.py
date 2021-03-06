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
conn = engine.connect()

print(db.Tables['Users'].join(db.Tables['Addresses']))
print(db.Tables['Users'].join(db.Tables['Addresses'], db.Tables['Users'].c.Id == db.Tables['Addresses'].c.UserId))
s = sqlalchemy.sql.select([db.Tables['Users'].c.Id, db.Tables['Addresses'].c.MailAddress]).select_from(
    db.Tables['Users'].join(db.Tables['Addresses'], db.Tables['Users'].c.Id == db.Tables['Addresses'].c.UserId)
)
print(s)
for row in conn.execute(s): print(row)

"""
u1 = db.Tables['Users'].alias()
u2 = db.Tables['Users'].alias()
s = sqlalchemy.sql.select([u1, u2]).where(u1.c.Id == u2.c.Id)
print(s)
for row in conn.execute(s): print(row)
"""
