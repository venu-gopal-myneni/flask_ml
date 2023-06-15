import requests

def hi():
    out = requests.get("http://127.0.0.1:5000")
    print(out.content)


def all_tenants():
    out = requests.get("http://127.0.0.1:5000/tenants")
    print(out.raw)


def add_tenant():
    # add tenant and get id details
    r = requests.post('http://127.0.0.1:5000/add_tenant', json=dict(tenantname="Venu Wick",email ="venuman@continentalcom"))
    print(r.content)

def add_model_eval():
    # add model
    pass

def print_all():
    pass    

if __name__ == "__main__":
    #add_tenant()
    all_tenants()
