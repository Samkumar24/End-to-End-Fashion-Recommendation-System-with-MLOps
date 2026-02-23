import os
import sys
from box import Box
from ensure import ensure_annotations
from pathlib import Path
import yaml
from src.recommendation_system.logging import logger

@ensure_annotations
def read_yaml(pathlib : Path):

    with open(pathlib) as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
        logger.info(f"yaml file: {pathlib} loaded successfully")
    
    return Box(yaml_content)

@ensure_annotations
def create_dir(pathlib_to_dir : list):

      for roles in pathlib_to_dir:
        os.makedirs(roles , exist_ok=True)
        logger.info(f"created directory at: {roles}")