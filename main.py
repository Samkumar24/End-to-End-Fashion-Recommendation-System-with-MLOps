from stage_pipline.stage_01_Data_injestion import Data_injestion_pipline
from stage_pipline.stage_02_Data_validation import Data_vaidation_pipline
from stage_pipline.stage_03_data_transformation import Data_transformation_pipline
from stage_pipline.stage_04_feature_enginerring import feature_enginerring_pipline
from stage_pipline.stage_05_model_training import model_training_pipline
from stage_pipline.stage_06_model_eval import model_eval_pipline
from src.recommendation_system.logging import logger


# ── Stage 1 — Data Ingestion ──────────────────────────
Stage_name = "Stage 1 : Data Ingestion"
try:
    logger.info("")
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  STARTED  <<<<<<")
    logger.info("=" * 80)
    data_ingestion = Data_injestion_pipline()
    data_ingestion.main()
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  COMPLETED  <<<<<<")
    logger.info("=" * 80)
    logger.info("")
except Exception as e:
    logger.exception(e)
    raise e


# ── Stage 2 — Data Validation ─────────────────────────
Stage_name = "Stage 2 : Data Validation"
try:
    logger.info("")
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  STARTED  <<<<<<")
    logger.info("=" * 80)
    data_validation = Data_vaidation_pipline()
    data_validation.main()
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  COMPLETED  <<<<<<")
    logger.info("=" * 80)
    logger.info("")
except Exception as e:
    logger.exception(e)
    raise e


# ── Stage 3 — Data Transformation ────────────────────
Stage_name = "Stage 3 : Data Transformation"
try:
    logger.info("")
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  STARTED  <<<<<<")
    logger.info("=" * 80)
    data_transformation = Data_transformation_pipline()
    data_transformation.main()
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  COMPLETED  <<<<<<")
    logger.info("=" * 80)
    logger.info("")
except Exception as e:
    logger.exception(e)
    raise e


# ── Stage 4 — Feature Engineering ────────────────────
Stage_name = "Stage 4 : Feature Engineering"
try:
    logger.info("")
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  STARTED  <<<<<<")
    logger.info("=" * 80)
    feature_engineering = feature_enginerring_pipline()
    feature_engineering.main()
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  COMPLETED  <<<<<<")
    logger.info("=" * 80)
    logger.info("")
except Exception as e:
    logger.exception(e)
    raise e


# ── Stage 5 — Model Training ──────────────────────────
Stage_name = "Stage 5 : Model Training"
try:
    logger.info("")
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  STARTED  <<<<<<")
    logger.info("=" * 80)
    model_training = model_training_pipline()
    model_training.main()
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  COMPLETED  <<<<<<")
    logger.info("=" * 80)
    logger.info("")
except Exception as e:
    logger.exception(e)
    raise e


# ── Stage 6 — Model Evaluation ────────────────────────
Stage_name = "Stage 6 : Model Evaluation"
try:
    logger.info("")
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  STARTED  <<<<<<")
    logger.info("=" * 80)
    model_eval = model_eval_pipline()
    model_eval.main()
    logger.info("=" * 80)
    logger.info(f"          >>>>>>  {Stage_name}  COMPLETED  <<<<<<")
    logger.info("=" * 80)
    logger.info("")
except Exception as e:
    logger.exception(e)
    raise e