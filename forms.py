from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, TelField
from wtforms.validators import DataRequired, Email, Regexp

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(message="Please enter your name.")])
    email = StringField("Email", validators = [DataRequired(message="Please enter your email."), Email()])
    phone = TelField("Phone")
    message = TextAreaField("Message",validators = [DataRequired(message="Please share some details about your request.")])
    submit = SubmitField("Send")
