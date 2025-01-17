from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,SelectField,SubmitField

from wtforms.validators import DataRequired
class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    num_of_beds = StringField('No. of Rooms', validators=[DataRequired()])
    num_of_baths = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    propertyType  = SelectField('Property Type',choices=[('house','House'),('apartment','Apartment')])
    description = StringField('Description',validators=[DataRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'],"Browse")])

    
    submit = SubmitField("Add Property")
