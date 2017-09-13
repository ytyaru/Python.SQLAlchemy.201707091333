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

# and_, or_, not_
print(sqlalchemy.sql.and_(0 < db.Tables['Addresses'].c.Id, db.Tables['Addresses'].c.MailAddress.like('%mail%')))
# like
s = sqlalchemy.sql.select([db.Tables['Addresses']]).where(db.Tables['Addresses'].c.MailAddress.like('%mail%'))
print(s)
for row in conn.execute(s): print(row)

# between
s = sqlalchemy.sql.select([db.Tables['Addresses']]).where(
    sqlalchemy.sql.and_(
        db.Tables['Addresses'].c.Id.between(10, 20),
        db.Tables['Addresses'].c.MailAddress.like('%mail%')))
print(s)
for row in conn.execute(s): print(row)

# label, max()
s = sqlalchemy.sql.select([sqlalchemy.func.max(db.Tables['Addresses'].c.Id).label('MaxId')])
print(conn.execute(s).fetchone()['MaxId'])
print(conn.execute(s).scalar())
