import os
from src.recommendation_system.utils.common import read_yaml , create_dir
from src.recommendation_system.logging import logger
from src.recommendation_system.constants import CONFIG_PATH
from src.recommendation_system.entity import (Data_injestion_config ,
                                              Data_transformation_config,
                                              Data_validation_config,
                                              model_building_config,
                                              model_evalulation_config,
                                              feature_enginerring_config
                                        )

class Config_manager:

    def __init__(self , config_path = CONFIG_PATH):
        self.config_path = read_yaml(config_path)

        create_dir([self.config_path.artifacts_root])

##########################################################################

    def get_data_ingestion_config(self) -> Data_injestion_config:

        config = self.config_path.data_ingestion

        create_dir([config.raw_data , config.ingested_data])

        data_ingestion_config =  Data_injestion_config(

            dataset_link= config.dataset_link,
            raw_data      = (config.raw_data),
            ingested_data = (config.ingested_data)
            
        )

        return data_ingestion_config
##########################################################################

    def get_data_validation_config(self) -> Data_validation_config:

        config = self.config_path.data_validation

        create_dir([config.validated_data , 
                    config.fallback_data,
                    os.path.dirname(config.log_path)])
        
        data_validation_config = Data_validation_config(
        raw_data_path =     config.raw_data_path,
        validated_data     = config.validated_data,
        fallback_data      = config.fallback_data,
        log_path           = config.log_path,
        expected_columns   = config.expected_columns,
        missing_thresholds = dict(config.missing_thresholds),
        volume             = dict(config.volume),
        valid_aesthetics   = config.valid_aesthetics,
        range_checks       = dict(config.range_checks),
)
        return data_validation_config
    
##########################################################################
    
    def get_data_transformation(self) -> Data_transformation_config:
        
        config = self.config_path.data_transformation
        
        create_dir([config.transformed_data,
                    config.model_path])

        data_transformation_config = Data_transformation_config(
            valid_data = config.valid_data,
            transformed_data=config.transformed_data,
            model_path=config.model_path
        )

        return data_transformation_config
    
##########################################################################
    
    def get_feature_engineering(self) -> feature_enginerring_config:

        config = self.config_path.feature_engineering          

        create_dir([config.featured_data,                 
                config.model_path])

        feature_engineering_config = feature_enginerring_config( 
        transformed_model = config.transformed_model,
        featured_data    = config.featured_data,
        model_path       = config.model_path,
        sim_matrix_path  = config.sim_matrix_path,
        tfidf_path       = config.tfidf_path,
        scaler_path      = config.scaler_path,
        featured_df_path = config.featured_df_path,

    )

        return feature_engineering_config   

##########################################################################

    def get_model_building(self) -> model_building_config:
        
        config = self.config_path.model_building

        create_dir([config.model_path])

        return model_building_config (
            sim_matrix_path  = (config.sim_matrix_path),
            featured_df_path = (config.featured_df_path),
            model_path       = (config.model_path)
        )
                
    
##########################################################################

    def get_model_evaluation(self) -> model_evalulation_config:
        config = self.config_path.model_evalvation

        create_dir([config.model_eval_metrics])

        return model_evalulation_config(
            sim_matrix_path        = (config.sim_matrix_path),
            featured_df_path       = (config.featured_df_path),
            model_eval_metrics = (config.model_eval_metrics),
            ml_flow_tracking_uri   = config.ml_flow_tracking_uri,
        ml_flow_experiment_name = config.ml_flow_experiment_name,
        ml_flow_run_name        = config.ml_flow_run_name
        ) 
    

        

    