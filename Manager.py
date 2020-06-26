# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:15:45 2020

@author: ashud
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import CI
from importlib import reload
reload(CI)


#database_URI = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
#engine = create_engine(database_URI, echo=True)

class DBManager:
    

    def __init__(self, URI):
        self.URI = URI
        self.engine = create_engine(URI, echo=True)
        #Session = sessionmaker(bind=self.engine)
        #self.session = Session()
        
    def addAllTables(self):
        CI.base.metadata.create_all(self.engine)
        
    def print_tables_from_metadata(self):
        #prints out dictionary of all the tables in CI.py
        #print(CI.base.metadata.tables)
        #print(CI.Course.__tablename__)
        #use this method to make a list of just the table names for the unittests
        lisT = []
        for key in CI.base.metadata.tables:
            lisT.append(key)
        return lisT
    
    def addSingleTable(self, table):
        CI.base.metadata.create_all(self.engine, tables = [table])
        
    def dropSingleTable(self, tablename):
        table = CI.base.metadata.tables.get(tablename)
        CI.base.metadata.drop_all(self.engine, [table])
        
    def dropAllTables(self):
        CI.base.metadata.drop_all(self.engine)
        

database_URI = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
db = DBManager(database_URI)
temp = db.print_tables_from_metadata()
#print(temp)
#db.addSingleTable(CI.Course.__table__)

        

        


