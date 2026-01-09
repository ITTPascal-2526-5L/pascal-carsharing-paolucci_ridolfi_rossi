from . import db

class Driver(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    id_license = db.Column(db.String(20), nullable=False, primary_key=True)
    rating = db.Column(db.Float, nullable=True)
    earning = db.Column(db.Float, nullable=True)
    file_license = db.Column(db.String(100), nullable=True)  # Path del file della patente caricata

    def __repr__(self):
        return f'<Driver: {self.id} - Name: {self.name} {self.surname} - Mail: {self.mail} - Age: {self.age} - License: {self.id_license} - Rating: {self.rating} - Earning: {self.earning} - File License: {self.file_license}>'