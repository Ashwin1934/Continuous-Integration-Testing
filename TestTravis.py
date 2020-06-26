# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:30:45 2020

@author: ashud
"""


import unittest
import Manager
from CI import Course

emptylist = ['alembic_version', 'stockprices']
fulllist = ['alembic_version', 'courses', 'stockprices', 'students']

class Tests(unittest.TestCase):
    
    """
      Test for adding all ORM tables. The resultant list should have every table
      in CI.py and any existing tables on the MySQL db. 
    """
    
    def test_add_all_tables(self):
        db_uri = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
        dbm = Manager.DBManager(db_uri)
        dbm.dropAllTables()
        before = dbm.engine.table_names()
        dbm.addAllTables()
        after = dbm.engine.table_names()
        #this is a list of all tables in CI.py
        metadatatables = dbm.print_tables_from_metadata
        expected = metadatatables.copy()
        expected.update(before)
        print(expected)
        print(after)
        self.assertEqual(after, expected)
    
    @unittest.skip("Temporary")
    def test_drop_all_tables(self):
       db_uri = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
       dbm = Manager.DBManager(db_uri)
       dbm.dropAllTables()
       result = dbm.engine.table_names()
       self.assertEqual(result, emptylist)
    @unittest.skip("Temporary")
    def test_add_single_table(self):
        db_uri = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
        dbm = Manager.DBManager(db_uri)
        dbm.addSingleTable(Course.__table__)
        listtables = dbm.engine.table_names()
        self.assertIn(Course.__tablename__, listtables)
    
    @unittest.skip("temp")
    def test_drop_single_table(self):
        db_uri = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
        dbm = Manager.DBManager(db_uri)
        dbm.dropSingleTable(Course.__tablename__)
        result = dbm.engine.table_names()
        self.assertEqual(result, emptylist)

        
       
       
        
        
        
if __name__ == '__main__':
    unittest.main()
        
    

        
        
        



