from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,TextAreaField,SelectField

from wtforms.validators import InputRequired
class CreateProperty(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    numofbeds = StringField('No. of Rooms', validators=[InputRequired()], render_kw={"placeholder":"3"})
    numofbaths = StringField('No. of Bathrooms', validators=[InputRequired()], render_fw={"placeholder":"2"})
    location = StringField('Location', validators=[InputRequired()], render_kw={"placeholder":"10 Waterloo Rd"})
    price = StringField('Price', validators=[InputRequired()], render_fw={"placeholder":"15,000,000"})
    propertyType  = SelectField('Property Type',choices=[('House','House'),('Apartment','Apartment')])
    description = TextAreaField('Description',validators=[InputRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png',"Browse"])])

    
