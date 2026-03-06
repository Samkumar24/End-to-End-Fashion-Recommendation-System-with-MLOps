from src.recommendation_system.config.config import Config_manager
from src.recommendation_system.components._04_feature_enginerring import feature_enginerring_config



class feature_enginerring_pipline:

    def __init__(self):
        pass

    def main():


        con = Config_manager()
        feature_eng = con.get_feature_engineering()
        feature_eng = feature_enginerring_config(feature_eng)
        feature_eng.initiate_feature_engineering()