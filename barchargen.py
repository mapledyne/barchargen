from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hQCPJ-MZLziN9ysoJKC-pgWX-.JU-'

class BarCodeForm(FlaskForm):
    barcode = StringField('Barcode', validators=[DataRequired()])
    submit = SubmitField('Make me!')

@app.route("/")
def default_page():
    form = BarCodeForm()
    return render_template('main.html', title='BarCharGen', form=form)


@app.route("/ping")
def ping():
    return "pong"

app.run (host = "172.21.0.4", port = 5000)

