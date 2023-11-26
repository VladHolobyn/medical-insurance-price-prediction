from app.main import bp
from flask import render_template
from app.form import Form
import pickle
import os

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@bp.route('/', methods=['POST', 'GET'])
def info():
    form = Form()
    result = ""
    if form.validate_on_submit():
        smoking_value = 1 if form.smoking.data else 0
        location_choices = {
            choice[0]: 0 if choice[0] not in form.location.data else 1 for choice in form.location.choices
            }
        result = round(model.predict([[
            form.age.data,
            int(form.gender.data),
            form.bmi.data,
            form.children.data,
            smoking_value,
            location_choices.get("northeast"),
            location_choices.get("northwest"),
            location_choices.get("southeast"),
            location_choices.get("southwest")]
            ][0]),2)
    return render_template("index.html",form=form,result=result)

