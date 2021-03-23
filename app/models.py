from . import db
import enum
from sqlalchemy import Integer, Enum


class PropertyTypes(enum.Enum):
    """Defines the property types."""
    apartment = 'apartment'
    house = 'house'


class PropertyModel(db.Model):
    """The model for a housing property."""

    __tablename__ = 'properties'

    # Defining attributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    num_of_beds = db.Column(db.Integer)
    description = db.Column(db.String(500))
    num_of_baths = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Numeric(10, 2))
    photo = db.Column(db.String(255))
    propertyType = db.Column(Enum(PropertyTypes))

    # Initializing the Model, **kwargs is used to accept all arguments given
    def __init__(
            self, title, num_of_beds, num_of_baths, description,
            price, location, propertyType, photo):

        super().__init__()

        self.title = title
        self.num_of_beds = num_of_beds
        self.num_of_baths = num_of_baths
        self.description = description
        self.num_of_beds = num_of_beds
        self.num_of_baths = num_of_baths
        self.price = price
        self.propertytype = propertytype
        self.location = location
        self.propertyType = propertyType
        self.photo= photo