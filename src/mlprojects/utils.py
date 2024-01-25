import os
import sys
from src.mlprojects.exception import customexception
from src.mlprojects.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host =os.getenv("host")
user =os.getenv("user")
password =os.getenv("password")
db =os.getenv("db")

def read_sql_data():
    try:
            logging.info("Connection Started ")
            mydb=pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=db
            )
            logging.info("Connection established",mydb)
            df=pd.read_sql_query("SELECT * FROM `students`",mydb)
            print(df.head())
            return df
    except Exception as e :
            raise customexception(e,sys)