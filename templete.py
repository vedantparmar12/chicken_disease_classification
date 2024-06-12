import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name= "cnnClassifier"
list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.Py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml" "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templetes/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    '''Spliting folder and file'''

    if filedir != "":
        os.makedirs(filedir,exist_ok=True) # exist_ok =True means if it exist it will not replaced
        logging.info(f"Creating folder {filedir} for the file {filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File {filepath} already exists")