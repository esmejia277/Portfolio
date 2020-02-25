from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError, Length

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[ DataRequired()])
    email = StringField(label='Email', validators=[ DataRequired(), Email() ])
    message = TextAreaField(label='Message', validators=[ DataRequired(),
        Length(min=20, message="Message must be at least 20 characters long.") 
    ])