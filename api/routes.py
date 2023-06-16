
from api.models import Tenant,Metadata
from api import app,db
from flask import request
from api.utils import process_list

@app.route("/home")
def hi_world():
    return "<p>Hello, World!</p>"

@app.route("/tenants" )
def get_all_tenants():
    tenants = Tenant.query.all()
    data = process_list(tenants)
    return {'message': 'success','data':data}


@app.route("/metadata" )
def get_all_metadata():
    meta = Metadata.query.all()
    data = process_list(meta)
    return {'message': 'success','data':data}



@app.route('/add_metadata',methods=['POST'])
def add_metadata():
    data_dict = dict(request.get_json())
    mt = Metadata(**data_dict)
    db.session.add(mt)
    db.session.commit()

    return {'message': 'success'}


@app.route('/add_tenant',methods=['POST'])
def add_tenant():
    data_dict = dict(request.get_json())
    te = Tenant(**data_dict)
    db.session.add(te)
    db.session.flush()
    db.session.refresh(te)
    db.session.commit()

    return {'message': 'success','id':te.id}

