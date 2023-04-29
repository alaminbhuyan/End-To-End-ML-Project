from mlproject import logger
from mlproject.pipeline import DataIngestionTrainingPipeline
import sys
from mlproject.exception import CustomException


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(msg=f">>>> Stage {STAGE_NAME} Started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(msg=f">>>> Stage {STAGE_NAME} Completed <<<<")
except Exception as e:
    logger.exception(msg=e)
    raise e