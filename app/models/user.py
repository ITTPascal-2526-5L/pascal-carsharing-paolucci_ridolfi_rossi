# from . import db
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     surname = db.Column(db.String(50), nullable=False)
#     mail = db.Column(db.String(50), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     created_date = db.Column(db.DateTime, default=db.func.current_timestamp())

#     def __repr__(self):
#         return f'<User {self.id} - Name: {self.name} {self.surname} - Mail: {self.mail} - Age: {self.age}>'