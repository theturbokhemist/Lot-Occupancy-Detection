##IMPORTS##
import os
#module to interact with the operating system

from pathlib import Path 
# The pathlib module provides a more modern and user-friendly way to work with file paths and directories compared to the traditional os.path module.

import logging
#python standard library and provides flexible framework for emitting log messages from your code.

#LOGGING
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
#This sets the logging level to INFO, which means only messages with an INFO level or higher will be logged. INFO is a standard level for informational messages.

project_name = "lot_occupancy_detection"

list_of_files = [

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

#.github/workflows is for when youre doing the deployment, all the CI/CD code commands go here, yaml file
#the .gitkeep is so that its not empty when you do the commit. gitkeep will be removed once yaml is created


def create_file_structure():
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = filepath.parent, filepath.name

        #When used in a boolean context, an empty Path object evaluates to False.
        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file {filename}")

        if not filepath.exists() or filepath.stat().st_size == 0:
            with filepath.open("w"):
                pass
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"{filename} already exists")

if __name__ == "__main__":
    create_file_structure()