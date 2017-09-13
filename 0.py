#!python3
#coding: utf-8
#http://docs.sqlalchemy.org/en/latest/core/tutorial.html
import sqlalchemy
#from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
print(sqlalchemy.__version__)
engine = sqlalchemy.create_engine('sqlite:///' + '0.db')
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table('Users', metadata,
        sqlalchemy.Column('Id', sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column('Name', sqlalchemy.String))
addrs = sqlalchemy.Table('Addresses', metadata,
        sqlalchemy.Column('Id', sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column('UserId', None, sqlalchemy.ForeignKey('Users.Id')),
        sqlalchemy.Column('MailAddress', sqlalchemy.String))
metadata.create_all(engine)

