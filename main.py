import os
from dotenv import load_dotenv
import requests
from api.ml import ml_main
import api.models

def hi():
    out = requests.get("http://127.0.0.1:5000")
    print(out.content)


def all_tenants():
    out = requests.get("http://127.0.0.1:5000/tenants")
    for te in out:
        print(te)


def add_tenant(tn,email):
    # add tenant and get id details
    r = requests.post('http://127.0.0.1:5000/add_tenant', json=dict(tenantname=tn,email =email))
    return dict(r.json())

def add_model_eval(filename,eval,tenant_id):
    # add model
    r = requests.post('http://127.0.0.1:5000/add_metadata', json=dict(filename=filename,eval=eval,tenant_id=tenant_id))
    return dict(r.json())

def print_all():
    pass    

def get_env():
    load_dotenv()
    TENANT_NAME = os.getenv('TENANT_NAME')
    TENANT_EMAIL = os.getenv('TENANT_EMAIL')

    CSV_FILE_PATH = os.getenv('CSV_FILE_PATH')
    Y_COLUMN = os.getenv('Y_COLUMN')

    return TENANT_NAME,TENANT_EMAIL,CSV_FILE_PATH,Y_COLUMN

if __name__ == "__main__":
    TENANT_NAME,TENANT_EMAIL,CSV_FILE_PATH,Y_COLUMN = get_env()
    ## Add a tenant
    out = add_tenant(TENANT_NAME,TENANT_EMAIL)
    ten_id = out["id"]
    print(out)
    
    ## run ml model
    eval = ml_main(CSV_FILE_PATH,Y_COLUMN)
    print(eval)

    ## add metadata
    out = add_model_eval(CSV_FILE_PATH,eval,ten_id)
    print(out)
    ## all tenants

    ## all metadata




