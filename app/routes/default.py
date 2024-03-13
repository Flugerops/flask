from .. import app
from flask import render_template

@app.route("/")
def index():    
    return render_template("_index.html")

@app.route("/menu")
def menu():

    return render_template("menu.html")