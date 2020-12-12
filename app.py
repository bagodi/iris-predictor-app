import joblib
import os

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='wP4xQ8hUljJ5oI1c'
bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    sepal_length = FloatField('sepal_length: ', validators=[DataRequired()])
    sepal_width = FloatField('sepal_width: ', validators=[DataRequired()])
    petal_length = FloatField('petal_length: ', validators=[DataRequired()])
    petal_width = FloatField('petal_width: ', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    specie = 'No-image'
    if form.validate_on_submit():
        x = [[form.sepal_length.data, form.sepal_width.data, form.petal_length.data, form.petal_width.data]]
        specie = make_prediction(x)
    return render_template('index.html', form=form, specie=specie)

def make_prediction(x):
    filename = os.path.join('model','finalized_model.sav')
    model = joblib.load(filename)
    return model.predict(x)[0]