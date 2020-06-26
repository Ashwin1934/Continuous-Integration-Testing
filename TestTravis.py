# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:30:45 2020

@author: ashud
"""


import unittest
import Manager

emptylist = ['alembic_version', 'stockprices']
fulllist = ['alembic_version', 'courses', 'stockprices', 'students']

class Tests(unittest.TestCase):
    
    
    def test_add_all_tables(self):
        db_uri = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
        dbm = Manager.DBManager(db_uri)
        dbm.addAllTables()
        result = dbm.engine.table_names()
        self.assertEqual(result, fulllist)
        
    def test_drop_all_tables(self):
       db_uri = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
       dbm = Manager.DBManager(db_uri)
       dbm.dropAllTables()
       result = dbm.engine.table_names()
       self.assertEqual(result, emptylist)
       
    def test_add_S
       
        
        
        
if __name__ == '__main__':
    unittest.main()
        
    

        
        
        



