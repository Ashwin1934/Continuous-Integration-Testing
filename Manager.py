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

print(CI.str)



#database_URI = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
#engine = create_engine(database_URI, echo=True)

class DBManager:
    
    
    
    def __init__(self, URI):
        self.URI = URI
        self.engine = create_engine(URI, echo=True)
        #Session = sessionmaker(bind=self.engine)
        #self.session = Session()
        
    def testingprint(self):
        print(CI.str)
        
    def addAllTables(self):
        print('TEST')
        CI.base.metadata.create_all(self.engine)
        
    def dropSingleTable(self, tablename):
        table = CI.base.metadata.tables.get(tablename)
        CI.base.metadata.drop_all(self.engine, [table])
        
    def dropAllTables(self):
        CI.base.metadata.drop_all(self.engine)
        


