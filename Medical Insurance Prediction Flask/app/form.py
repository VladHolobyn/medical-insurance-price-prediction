from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,IntegerField,BooleanField,RadioField,SelectField
from wtforms.validators import DataRequired, Email 

class Form(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired()])
    bmi = StringField('BMI', validators=[DataRequired()])
    children = IntegerField('Children', validators=[DataRequired()])
    smoking = BooleanField("Are you smoker?")
    gender =  RadioField('Select your gender', choices=[('male','Male'),('female','Female')])
    location = SelectField(u'Select your location', choices=[('northeast', 'northeast'), ('northwest', 'northwest'), ('southeast', 'southeast'), ('southwest', 'southwest')])
    submit = SubmitField('Send')