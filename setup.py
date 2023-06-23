from setuptools import setup
from typing import List

def get_requirements_list():

    """this function is going to return list of requirements mentioned in requirements.txt
    this function is going to return list which contains name of libraries in requirements,txt"""

    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

# declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Vinayak D"
DESCRIPTION = "First Project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES, 
install_requires=get_requirements_list()
)