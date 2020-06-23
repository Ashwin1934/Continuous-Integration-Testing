# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:15:45 2020

@author: ashud
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ContinuousIntegrationPlayground as CP
import Course

course = Course(5, 'Ashwin')
print(course)


#database_URI = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
#engine = create_engine(database_URI, echo=True)

"""
class DBManager:
    
    def __init__(self, URI):
        self.URI = URI
        self.engine = create_engine(URI, echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
    def addAllTables(self):
        print('TEST')
        base.metadata.create_all(self.engine)
        
    def dropAllTables(self):
        base.metadata.drop_all(self.engine)
        
    def dropSingleTable(self, tablename):
        table = base.metadata.tables.get(tablename)
        base.metadata.drop_all(self.engine, [table])
        
db_uri = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
dbm = DBManager(db_uri)
#dbm.dropAllTables()
#dbm.addAllTables()
#dbm.dropAllTables()
print(dbm.engine.table_names())
dbm.addAllTables()
print(dbm.engine.table_names())
"""
