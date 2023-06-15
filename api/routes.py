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
    data_dict = request.get_json().__dict__
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
    print(te,te.id)
    db.session.commit()

    return {'message': 'success'}

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#         te1 = Tenant(tenantname="John Wick",email ="boogeyman@continental.com")
#         db.session.add(te1)
#         db.session.commit()

#         te1=Tenant.query.filter_by(tenantname="John Wick").all()[0]

#         mt = Metadata(filename="abc.csv",eval=str({"key":"value"}),tenant_id=te1.id)
#         db.session.add(mt)
#         db.session.commit()


#         tes = Tenant.query.all()
#         for te in tes:
#             print(te)
#             print(te.models)
