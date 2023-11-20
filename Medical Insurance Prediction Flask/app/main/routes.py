from app.main import bp
from flask import render_template
from app.form import Form


@bp.route('/', methods=['POST', 'GET'])
def info():
    form = Form()
    result = ""
    if form.validate_on_submit():
        age = form.age.data
        bmi = form.bmi.data
        children = form.children.data
        smoking = form.smoking.data
        gender = form.gender.data
        location = form.location.data
        result = age + int(bmi)
    return render_template("index.html",form=form,result=result)

