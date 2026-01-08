from user import User
from . import db
class Driver(User):
    id_license = db.Column(db.String(20), nullable=False, primary_key=True)
    rating = db.Column(db.Float, nullable=True)
    earning = db.Column(db.Float, nullable=True)
    file_license = db.Column(db.String(100), nullable=True)  # Path del file della patente caricata

    def __repr__(self):
        return f'<Driver: {self.id} - Name: {self.name} {self.surname} - Mail: {self.mail} - Age: {self.age} - License: {self.id_license} - Rating: {self.rating} - Earning: {self.earning} - File License: {self.file_license}>'