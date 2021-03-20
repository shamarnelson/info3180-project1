from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,TextAreaField,SelectField

from wtforms.validators import InputRequired
class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    numofbeds = StringField('No. of Rooms', validators=[InputRequired()])
    numofbaths = StringField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    propertyType  = SelectField('Property Type',choices=[('House','House'),('Apartment','Apartment')])
    description = TextAreaField('Description',validators=[InputRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png',"Browse"])])

    
