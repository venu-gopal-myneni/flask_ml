import requests
from api.ml import ml_main

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

if __name__ == "__main__":
    ## Add a tenant
    tenantname = "a22sdgvdsgb1c"
    email = "11sfadsgsafas"
    out = add_tenant(tenantname,email)
    ten_id = out["id"]
    print(out)
    
    ## run ml model
    file_path=r"C:\Users\shenron\projects\flask_ml\csv_data\real_estate.csv"
    target_column = 'Y house price of unit area'
    eval = ml_main(file_path,target_column)
    print(eval)

    ## add metadata
    out = add_model_eval(file_path,eval,ten_id)
    print(out)
    ## all tenants

    ## all metadata




