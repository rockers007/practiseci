import os
import sys
from src.mlprojects.exception import customexception
from src.mlprojects.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pymysql

import pickle
import numpy as np
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
        
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e :
            raise customexception(e,sys)     