from . import db


class UserProperty(db.Model):
    
    __tablename__ = 'user_property'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    numofbed= db.Column(db.String(80))
    numofbath = db.Column(db.String(30))
    price = db.Column(db.String(80))
    propertytype = db.Column(db.String(29))
    location = db.Column(db.String(225))
    photo=db.Column(db.String(225), index=True)
    
    
    
    def __init__(self, title, description, numofbed, numofbath, price, propertytype, location, photo):
        self.title = title
        self.description = description
        self.numofbed = numofbed
        self.numofbath = numofbath
        self.price = price
        self.propertytype = propertytype
        self.location = location
        self.photo=photo



    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)