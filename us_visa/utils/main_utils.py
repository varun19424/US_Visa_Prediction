import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.load(yaml_file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exist(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    


def load_object(file_path:str) -> object:
    logging.info('Entering the load_object method of utils')

    try:
        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj)
        logging.info('Exited the load_object method of utils')
        return obj
    
    except Exception as e:
        raise USvisaException(e, sys) from e
    
