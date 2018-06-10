#!/usr/bin/env python3
'''Database intitialization code: Mapper  object and connecting to the database'''

import os
import sys
import pyscopg2

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#mapper
Base = declarative_base() #may also be metadata = MetaData()

class Person(Base):
    __tablename__ = 'ipave'
    id = Column (Integer, primary_key = True)
    ip_address = Column(String)
    subnet_mask = Column(String)
    subnet_inuse = Column()
    datasource = Column(String)
    aws_region = Column(String)
    aws_availability_zone = Column(String)
    aws_subnet_id = Column(String)
    aws_vpc_id = Column(String)


#connecting
#syntax to connect 'dialect+driver://username:password@host:port/database'
#dialect names are sqlite, mysql, postgresql, oracle, mssql
#driver name is the DBAPI used to connect to the database using all lowercase letters. Default is the most widely available driver. 
engine = create_engine('postgresql+psycopg3://   @127.0.0.1:5432/ipave.db', echo = True)


Base.metadata.createall(engine) #may also be metadata.create_all(engine)
#createall() creates tables in order of their dependency

#Check if the table exists
ipave.create(engine, = checkfirst = True)

object with a dictionary is created. then parse to make entries over the database. Then we connect to database to query, then return back in the same format as the dictionary
    #syntax to relate tables to table is field = Column(Integer, ForeignKey ('othertablename.id'))