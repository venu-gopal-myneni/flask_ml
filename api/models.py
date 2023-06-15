from api import db

class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tenantname = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    models = db.relationship('Metadata', backref='tenant', lazy=True)

    def __repr__(self):
        return f"Tenant('{self.tenantname}', '{self.email}')"


class Metadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    eval = db.Column(db.String(100), unique=False,nullable=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=False)

    def __repr__(self):
        return f"Metadata('{self.filename}', '{self.eval}', '{self.tenant_id}')"