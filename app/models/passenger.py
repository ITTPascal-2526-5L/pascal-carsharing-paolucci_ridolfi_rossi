from user import User
from . import db

class Passenger(User):
    pass

    def __repr__(self):
        return f'<Passenger {self.id} - Name: {self.name} {self.surname} - Mail: {self.mail} - Age: {self.age}>'