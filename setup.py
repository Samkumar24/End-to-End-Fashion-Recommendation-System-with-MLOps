import os
import sys
import logging
from pathlib import Path


project_name = "recommendation_system"


files = [

    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f"src/{project_name}/config/configuration.py"
    'main.py'
]

for item in files :
    file_path = Path(item)
    
    file_dir , file  = os.path.split(file_path)


    if file_dir != '':
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory:{file_dir} for the file {file}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path , 'w') as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file} is already exists")