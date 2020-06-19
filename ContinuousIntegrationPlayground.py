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

database_URI = 'mysql+pymysql://@localhost:3306/MyDatabase'
engine = create_engine(database_URI, echo=True)
