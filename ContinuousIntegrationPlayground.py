# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:30:39 2020

@author: ashud
"""
import sqlalchemy
import pymysql
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#database_URI = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
#engine = create_engine(database_URI, echo=True)

base = declarative_base()

#session = sessionmaker(bind=engine)()


#create a dummy table/class for testing purposes
class Course(base):
    __tablename__ = "Courses"
    number = Column('Course Number', Integer, primary_key=True)
    name = Column('Course Name', String(10))
    
    def __init__(self, number, name):
        self.number = number
        self.name = name
        
    def __repr__(self):
        return repr(str(self.number) +":"+self.name)
 
#second dummy table for testing purposes
class Students(base):
    __tablename__ = "Students"
    firstname = Column('First Name', String(10), primary_key=True)
    lastname = Column('Last Name', String(10))
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def __repr__(self):
        return repr(self.firstname + self.lastname)
 
        
#create a manager class to administrate
class DBManager:
    
    def __init__(self, URI):
        self.URI = URI
        self.engine = create_engine(URI, echo=True)
        
    def addTables(self):
        print('TEST')
        base.metadata.create_all(self.engine)
        
        
dbm = DBManager('mysql+pymysql://root:@localhost:3306/MyDatabase')
dbm.addTables()
print(dbm.URI)









    
    
