from src.recommendation_system.config.config import Config_manager
from src.recommendation_system.components._03_data_transformation import Data_transformation_check



class Data_transformation_pipline:

    def __init__(self):
        pass

    def main():


        con = Config_manager()

        data_transformation_config = con.get_data_transformation()
        data_transformation = Data_transformation_check(data_transformation_config)
        df = data_transformation.initiate_data_transformation()  