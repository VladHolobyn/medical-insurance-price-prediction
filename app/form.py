from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,BooleanField,RadioField,SelectField,FloatField
from wtforms.validators import DataRequired,ValidationError,InputRequired


def non_negative(form, field):
    if field.data is not None and field.data < 0:
        raise ValidationError('This field accepts only non-negative numbers.')
    

def adult_check(form, field):
    if field.data is not None and field.data < 18:
        raise ValidationError('Your age must be 18 or greater.')

class Form(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired(message="Field is empty or value isn`t integer number(must be greater than 17)."),adult_check])
    bmi = FloatField('Body Mass Index', validators=[DataRequired(message="Field is empty or value isn`t float number(must be greater than 0)."),non_negative])
    children = IntegerField('Children', validators=[InputRequired(message="Field is empty or value isn`t integer number."),non_negative])
    smoking = BooleanField("Are you smoker?")
    gender =  RadioField('Select your gender', choices=[('1','Male'),('0','Female')])
    location = SelectField(u'Select your location', choices=[('northeast', 'Northeast'), ('northwest', 'Northwest'), ('southeast', 'Southeast'), ('southwest', 'Southwest')])
    submit = SubmitField('Predict')
