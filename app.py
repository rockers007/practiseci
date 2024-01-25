from src.mlprojects.exception import customexception
from src.mlprojects.logger import logging
from src.mlprojects.components.data_ingestion import DataIngestion
from src.mlprojects.components.data_transformation import DataTransformationConfig,DataTransformation
from src.mlprojects.components.model_trainer import ModelTrainerConfig ,ModelTrainer
import sys

if __name__=="__main__":
    try:
       logging.info("Start APP")
    
       data_ingestion =DataIngestion()
       train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
       
       data_transformation=DataTransformation()
       train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)
       
       ## Model Training
       model_trainer=ModelTrainer()
       print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
    except Exception as e :
            raise customexception(e,sys)