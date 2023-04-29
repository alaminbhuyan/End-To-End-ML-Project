import os
import urllib.request as request
from zipfile import ZipFile
from pathlib import Path
from mlproject.entity import DataIngestionConfig
from mlproject import logger
from mlproject.utils import get_size



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    # let's create a function that will download the data
    def download_file(self):
        logger.info(msg="Trying to download file...")
        if not os.path.exists(path=self.config.local_data_file):
            logger.info(msg="Download Started...")
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, 
                filename=self.config.local_data_file)
            logger.info(msg=f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(msg=f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def unzip_file(self):
        logger.info(msg="Unziping Files...")
        with ZipFile(file=self.config.local_data_file, mode='r') as zf:
            zf.extractall(path=self.config.unzip_dir)