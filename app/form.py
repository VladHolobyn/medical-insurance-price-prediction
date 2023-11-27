from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,IntegerField,BooleanField,RadioField,SelectField,FloatField
from wtforms.validators import DataRequired, Email ,ValidationError


def non_negative(form, field):
    if field.data is not None and field.data < 0:
        raise ValidationError('This field accepts only non-negative numbers.')

class Form(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired(message="This field is required.Only integer numbers."),non_negative])
    bmi = FloatField('BMI', validators=[DataRequired(message="This field is required.Only float numbers."),non_negative])
    children = IntegerField('Children', validators=[DataRequired(message="This field is required.Only integer numbers."),non_negative])
    smoking = BooleanField("Are you smoker?")
    gender =  RadioField('Select your gender', choices=[('1','Male'),('0','Female')])
    location = SelectField(u'Select your location', choices=[('northeast', 'Northeast'), ('northwest', 'Northwest'), ('southeast', 'Southeast'), ('southwest', 'Southwest')])
    submit = SubmitField('Send')
