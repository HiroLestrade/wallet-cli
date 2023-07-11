import json
import os

def read_json():
    #If the file doesn't exist, 
    if not os.path.isfile('data.json'):
        with open('data.json', 'w') as file:
            json.dump({'cuentas': [], 'gastos': [], 'servicios': []}, file)
    #Then, read the file
    with open('data.json', 'r') as file:
        data = json.load(file)
    #and return the data
    return data

def write_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

__all__ = ['read_json', 'write_json']