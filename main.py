from stage_pipline.stage_01_Data_injestion import Data_injestion_pipline
from stage_pipline.stage_02_Data_validation import Data_vaidation_pipline
from stage_pipline.stage_03_data_transformation import Data_transformation_pipline
from stage_pipline.stage_04_feature_enginerring import feature_enginerring_pipline
from stage_pipline.stage_05_model_training import model_training_pipline
from stage_pipline.stage_06_model_eval import model_eval_pipline
from src.recommendation_system.logging import logger




# ==================================================================================
Stage_name = "Stage 6 : Model Evaluation"
try:
    logger.info("") 
    logger.info("="*80)
    logger.info(f"          >>>>>>  {Stage_name}  STARTED  <<<<<<")
    logger.info("="*80)
    model_eval = model_eval_pipline()
    model_eval.main()
    logger.info("="*80)
    logger.info(f"          >>>>>>  {Stage_name}  COMPLETED  <<<<<<")
    logger.info("="*80)
    logger.info("") 
except Exception as e:
    logger.exception(e)
    raise e
