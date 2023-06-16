from flask import Blueprint
from api.utils import process_list
from api.models import Tenant,Metadata

gets = Blueprint("gets",__name__)

@gets.route("/")
def hi_world():
    return "Welcome to ML App"

@gets.route("/tenants" )
def get_all_tenants():
    tenants = Tenant.query.all()
    data = process_list(tenants)
    return {'message': 'success','data':data}


@gets.route("/metadata" )
def get_all_metadata():
    meta = Metadata.query.all()
    data = process_list(meta)
    return {'message': 'success','data':data}
