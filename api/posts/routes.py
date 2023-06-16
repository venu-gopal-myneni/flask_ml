from flask import Blueprint
from api.models import Tenant,Metadata
from api import db
from flask import request


posts = Blueprint("posts",__name__)

@posts.route('/add_metadata',methods=['POST'])
def add_metadata():
    data_dict = dict(request.get_json())
    mt = Metadata(**data_dict)
    db.session.add(mt)
    db.session.commit()

    return {'message': 'success'}


@posts.route('/add_tenant',methods=['POST'])
def add_tenant():
    data_dict = dict(request.get_json())
    te = Tenant(**data_dict)
    db.session.add(te)
    db.session.flush()
    db.session.refresh(te)
    db.session.commit()

    return {'message': 'success','id':te.id}