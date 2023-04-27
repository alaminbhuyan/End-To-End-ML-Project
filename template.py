# Basically using thie template.py file we can create
# all the files and folders just one shot

# Import the necessary modules
import os
from pathlib import Path
import logging

# Specify logging configuration
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

# Specify the project name
project_name = "mlproject"

# Specify the all directories location
list_of_files = [
    # this file will help us to create CI-CD pipeline
    ".github/workflows/main.yaml",
    # ".github/workflows/.gitkeep",
    # we specify the __init__.py so that we can import any files from src folder
    # __init__.py folder treated as project module file
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    # this file contains all the basic functions and classes
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    # Handle the project different error or exception
    f"src/{project_name}/exception.py",
    "config/config.yaml",
    # params.yaml will be contains all the hyperparameters for the model
    "params.yaml",
    # requirements.txt file will be contains all packages required
    "requirements.txt",
    # setup.py used for consider all the files as a module that we will create
    # in src folder. so that we can import any files from src folder
    "setup.py",
    # this folder contains all the jupyter notebook files for testing purposes
    # before creating actual moduler coding
    "research/trials.ipynb"
]

for filepath in list_of_files:
    # Path class automatically recognized which operating system file path it is
    # based on the operating system it will maintain the path syntax
    filepath = Path(filepath)
    # split function split the directory and the file
    # Like: ["src/config", "demo.py"]
    filedir, filename = os.path.split(filepath)
    
    # if it is not empty directory then
    if filedir != "":
        os.makedirs(name=filedir, exist_ok=True)
        logging.info(msg=f"Creating directory: {filedir} for file: {filename}")
    
    # This logic will help to create if file is not existing or file size is zero
    # In that case it will create empty file
    if (not os.path.exists(path=filepath)) or (os.path.getsize(filename=filepath) == 0):
        with open(file=filepath, mode='w') as f:
            pass # creating an empty file only
            logging.info(msg=f"Creating empty file: {filepath}")
    else:
        logging.info(msg=f"{filename} is already exists")