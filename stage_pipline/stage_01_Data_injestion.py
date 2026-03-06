from src.recommendation_system.config.config import Config_manager
from src.recommendation_system.config.config import Data_injestion_config
from src.recommendation_system.components._01_data_injestion import Data_ingestion


class Data_injestion_pipline:

    def __init__(self):
        pass

    def main(self):
        con = Config_manager()
        data_ingestion = con.get_data_ingestion_config()
        data_ingestion = Data_ingestion(data_ingestion)
        data_ingestion.download_data()