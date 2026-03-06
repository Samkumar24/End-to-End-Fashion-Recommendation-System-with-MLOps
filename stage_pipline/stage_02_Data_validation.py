from src.recommendation_system.config.config import Config_manager
from src.recommendation_system.components._02_data_validation import Data_validation_check



class Data_vaidation_pipline:

    def __init__(self):
        pass

    def main(self):
        con = Config_manager()
        data_validation = con.get_data_validation_config()
        data_validation = Data_validation_check(data_validation)
        errors = data_validation.validate_data()
