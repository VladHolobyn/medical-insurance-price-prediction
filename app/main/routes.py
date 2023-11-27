from app.main import bp
from flask import render_template
from app.form import Form
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@bp.route('/', methods=['POST', 'GET'])
def info():
    form = Form()
    result = ""
    if form.validate_on_submit():
        location_choices = {
            choice[0]: False if choice[0] not in form.location.data else True for choice in form.location.choices
        }

        input_data = [
            form.age.data,
            int(form.gender.data),
            form.bmi.data,
            form.children.data,
            int(form.smoking.data),
            location_choices.get("northeast"),
            location_choices.get("northwest"),
            location_choices.get("southeast"),
            location_choices.get("southwest")
        ]

        # Scale the input using the loaded scaler
        scaled_input = scaler.transform([input_data])

        result = round(model.predict(scaled_input)[0], 2)

    return render_template("index.html", form=form, result=result)
