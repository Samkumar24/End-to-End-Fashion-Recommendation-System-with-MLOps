from src.recommendation_system.config.config import Config_manager
from src.recommendation_system.components._05_model_building import model_building_config



class Data_transformation_pipline:

    def __init__(self):
        pass

    def main():


        con = Config_manager()
        model_feature = con.get_model_building()
        model_feature = model_building_config(model_feature)
        df = model_feature.initiate_recommendation('men wonder sports running shoes',top_k=10)
        