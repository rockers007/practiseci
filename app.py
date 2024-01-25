from src.mlprojects.exception import customexception
from src.mlprojects.logger import logging
from src.mlprojects.components.data_ingestion import DataIngestion
from src.mlprojects.components.data_transformation import DataTransformationConfig,DataTransformation
import sys

if __name__=="__main__":
    try:
       logging.info("Start APP")
    
       data_ingestion =DataIngestion()
       train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
       
       data_transformation=DataTransformation()
       data_transformation.initiate_data_transormation(train_data_path,test_data_path)
       
    except Exception as e :
            raise customexception(e,sys)