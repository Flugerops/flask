from .. import app
from flask import render_template

@app.route("/")
def index():    
    return "<h1>HELLO, ZMIINI NOVATORI</h1>"

@app.route("/app1")
def index_app1():

    return render_template("_index.html")