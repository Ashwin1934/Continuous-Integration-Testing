# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:30:45 2020

@author: ashud
"""



"""class Tests(unittest.TestCase):
    def test_drop_tables(self):
        DBManager.dropAllTables(self)"""
        
db_uri = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
dbm = DBManager(db_uri)
print(dbm.URI)
        
        
        



