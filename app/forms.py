from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email


class PropertyForm(FlaskForm):
    property_title = StringField("Property Title", validators=[InputRequired()])
    number_of_bedrooms = StringField("No. of Bedrooms", validators=[InputRequired()])
    number_of_bathrooms = StringField("No. of Bathrooms", validators=[InputRequired()])
    location = StringField("Location", validators=[InputRequired()])
    price = StringField("Price", validators=[InputRequired()])
    description = TextAreaField("Description", validators=[InputRequired()], render_kw={"rows": "3"})
    type = SelectField("Property Type", choices=['House', 'Apartment'])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images Only!')])