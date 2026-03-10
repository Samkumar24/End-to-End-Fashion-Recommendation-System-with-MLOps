from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class Data_injestion_config:

    dataset_link : str
    raw_data : Path
    ingested_data : Path


@dataclass(frozen=True)
class Data_validation_config:
    raw_data_folder:    Path
    validated_data:     Path
    fallback_data:      Path
    log_path:           Path
    expected_columns:   list[str]
    missing_thresholds: dict[str, float]
    volume:             dict[str, int]
    valid_aesthetics:   list[str]
    range_checks:       dict[str, dict]


@dataclass(frozen=True)
class Data_transformation_config:
    valid_data : Path
    transformed_data: Path
    model_path : Path


@dataclass(frozen=True)
class feature_enginerring_config:
    transformed_model: Path
    featured_data:   Path
    model_path:      Path
    sim_matrix_path : Path
    tfidf_path :      Path
    featured_df_path :Path
    scaler_path : Path


@dataclass(frozen=True)
class model_building_config:
    sim_matrix_path:  Path    
    featured_df_path: Path    
    model_path:       Path    

@dataclass(frozen=True)
class model_evalulation_config:
    sim_matrix_path: Path
    featured_df_path :Path 
    model_eval_metrics : Path
    ml_flow_experiment_name :str
    ml_flow_run_name :str
    ml_flow_tracking_uri :str


