from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField,SubmitField, BooleanField,PasswordField, TextAreaField, validators,SelectField
from flask_wtf import FlaskForm

class AboutMeForm(FlaskForm):
    food = StringField('Food: ')
    job = StringField('Professional/Job: ')
    adj = StringField('Adjective: ')


    submit = SubmitField('Generate My Story')