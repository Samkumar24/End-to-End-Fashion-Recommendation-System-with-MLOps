from stage_pipline.stage_01_Data_injestion import Data_injestion_pipline
from stage_pipline.stage_02_Data_validation import Data_vaidation_pipline
from stage_pipline.stage_03_data_transformation import Data_transformation_pipline
from stage_pipline.stage_04_feature_enginerring import feature_enginerring_pipline
from stage_pipline.stage_05_model_training import model_training_pipline
from stage_pipline.stage_06_model_eval import model_eval_pipline
from src.recommendation_system.logging import logger




Stage_name = "Data ingestion"
try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<") 
    data_ingestion = Data_injestion_pipline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

##################################################

Stage_name = "Data Validation"
try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<") 
    data_transformation = Data_vaidation_pipline()
    data_transformation.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

##################################################


Stage_name = "Data Transformtion"
try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<") 
    model_eval = Data_transformation_pipline()
    model_eval.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

##################################################


Stage_name = "Feature eniginerring"
try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<") 
    model_eval = feature_enginerring_pipline()
    model_eval.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

##################################################


Stage_name = "Model Training"
try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<") 
    model_eval = model_training_pipline()
    model_eval.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

##################################################


Stage_name = "Model Evalulation"
try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<") 
    model_eval = model_eval_pipline()
    model_eval.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


