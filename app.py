from src.mlprojects.exception import customexception
from src.mlprojects.logger import logging
from src.mlprojects.components.data_ingestion import DataIngestion
import sys

if __name__=="__main__":
    try:
       logging.info("Start APP")
    
       data_ingestion =DataIngestion()
       data_ingestion.initiate_data_ingestion()
       
    except Exception as e :
            raise customexception(e,sys)