from . import db
class School:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    dominial_suffix = db.Column(db.String(30), nullable=False)