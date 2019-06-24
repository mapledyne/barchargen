from flask import Flask
from flask import render_template
from flask import redirect
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import chargen

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hQCPJ-MZLziN9ysoJKC-pgWX-.JU-'

class BarCodeForm(FlaskForm):
    barcode = IntegerField('Barcode', validators=[DataRequired(), NumberRange(0, 9999999999999999)])
    submit = SubmitField('Make me!')

@app.route("/", methods=['GET', 'POST'])
def default_page():
    form = BarCodeForm()
    if form.validate_on_submit():
        return redirect("/barcode/" + str(form.barcode.data))
    return render_template('main.html', title='BarCharGen', form=form)

@app.route("/barcode/<seed>")
def generate(seed):
    return render_template('chargen.html', barcode = seed, character = chargen.Chargen(seed))

@app.route("/ping")
def ping():
    return "pong"

app.run (host = "172.21.0.4", port = 5000)

