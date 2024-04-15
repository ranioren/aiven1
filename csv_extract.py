import os 
import logging
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Logging 
logger = logging.getLogger(__name__)
logger.info(NameError)

#retrieve NZ statistics
url = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-csv.csv'
x =pd.read_csv(url)

#Postgres sessions start
engine = create_engine('postgresql://avnadmin:AVNS_9GdPZ16Tky7zJHZuvBq@pg-1dbc84aa-ontheran-2746.b.aivencloud.com:21282/defaultdb?sslmode=require', echo=False)
session = sessionmaker(bind=engine)
session = session()

Base = declarative_base()

class nzstats1(Base):
    __tablename__ = 'nzstats1'

    id = Column(Integer, primary_key=True) 
    Year = Column(Integer)
    Industry_aggregation_NZSIOC= Column( String(50))
    Industry_code_NZSIOC= Column(String(50))
    Industry_name_NZSIOC= Column(String(255))
    Units= Column( String(255) )
    Variable_code= Column(String(255))
    Variable_name= Column(String(255))
    Variable_category= Column(String(255))
    Value= Column(Integer)
    Industry_code_ANZSIC06= Column(String(255))

Base.metadata.create_all(engine)

for i in range(x.size):
    if i > 0:
        #Initiate class instance
        nz = nzstats1(Year = x.Year[i], 
                #Industry_aggregation_NZSIOC = x.Industry_aggregation_NZSIOC[i],
                Industry_code_NZSIOC = x.Industry_code_NZSIOC[i],
                Industry_name_NZSIOC = x.Industry_name_NZSIOC[i],
                Units = x.Units[i],
                Variable_code = x.Variable_code[i],
                Variable_name = x.Variable_name[i],
                Variable_category = x.Variable_category[i],
                Value = x.Value[i]
                #Industry_code_ANZSIC06 = x.Industry_code_ANZSIC06[i]
                    )
        #Add to table
        session.add(nz)
        session.commit()
    