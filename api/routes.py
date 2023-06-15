import sys,os
sys.path.append(os.getcwd())

from api.models import Tenant,Metadata
from api import app,db
from flask import request

@app.route("/home")
def hi_world():
    return "<p>Hello, World!</p>"

@app.route("/tenants" )
def get_all_tenants():
    tenants = Tenant.query.all()
    return tenants



@app.route('/add_metadata',methods=['POST'])
def add_metadata():
    data_dict = dict(request.get_json())
    print(f"Metadata : {data_dict}")
    mt = Metadata(**data_dict)
    db.session.add(mt)
    db.session.commit()

    return {'message': 'success'}


@app.route('/add_tenant',methods=['POST'])
def add_tenant():
    data_dict = dict(request.get_json())
    print(f"Tenant : {data_dict}")
    te = Tenant(**data_dict)
    db.session.add(te)
    db.session.flush()
    db.session.refresh(te)
    print(f"Tenant : {te}")
    db.session.commit()

    return {'message': 'success','id':te.id}

