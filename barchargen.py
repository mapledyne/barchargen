from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def default_page():
    return render_template('main.html')


app.run (host = "172.21.0.4", port = 5000)

