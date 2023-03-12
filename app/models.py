from . import db
from werkzeug.security import generate_password_hash


class Property(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_title = db.Column(db.String)
    number_of_bedrooms = db.Column(db.Integer)
    number_of_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String)
    price = db.Column(db.Float)
    type = db.Column(db.String)
    description = db.Column(db.String)
    photo = db.Column(db.String)
   


    def __init__(self,property_title,number_of_bedrooms,number_of_bathrooms,location, price, description, type,photo ):
        self.property_title = property_title
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.location = location
        self.price = price
        self.description = description
        self.type = type
        self.photo = photo

    