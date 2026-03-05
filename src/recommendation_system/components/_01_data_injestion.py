from src.recommendation_system.utils.common import read_yaml , create_dir
from src.recommendation_system.logging import logger
from src.recommendation_system.constants import CONFIG_PATH
from src.recommendation_system.logging import logger
from src.recommendation_system.entity import Data_injestion_config
import requests
import os



class Data_ingestion:

    def __init__(self, config : Data_injestion_config):
        
        self.config = config

    
    def download_data(self):

        try:

            url = self.config.dataset_link
            
            file_name = os.path.basename(url)

            save_path = os.path.join(self.config.raw_data , file_name)
            
            response = requests.get(url)
            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    f.write(response.content)

                logger.info(f"Request {response.status_code} success")
                logger.info(f"Data saved to: {self.config.raw_data}")

            else:
                logger.info("Exceution falied with {response.status_code}")
                raise Exception(f"Download failed — Status: {response.status_code}")
                
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f" Error: {e}")

        
        