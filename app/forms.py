from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError, Length

def validate_name(form, field):
    data = field.data.replace(' ','')
    if not data.isalpha():
        raise ValidationError(
            message='Name can not contain numbers or special characters!'
        )
        

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[ DataRequired(), validate_name])
    email = StringField(label='Email', validators=[ DataRequired(), Email() ])
    message = TextAreaField(label='Message', validators=[ DataRequired(), Length(min=20) ])
