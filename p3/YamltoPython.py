#! /usr/bin/env python
"""this file converts .yaml to python obj"""
import yaml
def Yaml_Python(file_Path):
    file = open(file_Path, 'r+')
    py_output = yaml.safe_load(file)  # YAML to python
    return py_output

output = Yaml_Python('file.yaml')  # yaml file path
print(output)
print ('This file is written in python 2 for migration')
