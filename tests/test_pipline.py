from stage_pipline.stage_01_Data_injestion import Data_injestion_pipline
from stage_pipline.stage_02_Data_validation import Data_vaidation_pipline
from stage_pipline.stage_03_data_transformation import Data_transformation_pipline
from stage_pipline.stage_04_feature_enginerring import feature_enginerring_pipline
from stage_pipline.stage_05_model_training import model_training_pipline
from stage_pipline.stage_06_model_eval import model_eval_pipline

def test_data_ingestion():
    try:
        pipeline = Data_injestion_pipline()
        pipeline.main()
        assert True
    except Exception as e:
        assert False, f"Data Ingestion failed: {str(e)}"

def test_data_validation():
    try:
        pipeline = Data_vaidation_pipline()
        pipeline.main()
        assert True
    except Exception as e:
        assert False, f"Data Validation failed: {str(e)}"

def test_data_transformation():
    try:
        pipeline = Data_transformation_pipline()
        pipeline.main()
        assert True
    except Exception as e:
        assert False, f"Data Transformation failed: {str(e)}"

def test_feature_engineering():
    try:
        pipeline = feature_enginerring_pipline()
        pipeline.main()
        assert True
    except Exception as e:
        assert False, f"Feature Engineering failed: {str(e)}"

def test_model_training():
    try:
        pipeline = model_training_pipline()
        pipeline.main()
        assert True
    except Exception as e:
        assert False, f"Model Training failed: {str(e)}"

def test_model_evaluation():
    try:
        pipeline = model_eval_pipline()
        pipeline.main()
        assert True
    except Exception as e:
        assert False, f"Model Evaluation failed: {str(e)}"