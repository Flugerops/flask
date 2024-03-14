from .. import app
from flask import render_template

@app.route("/")
def index():    
    return render_template("_index.html", title="Zmiini Novatori")


@app.route("/results")
def results():
    max_score = 100
    test_name = "Name"
    students = [
    {
        "name": "Yaromyr",
        "score": 79
        
    },
    {
        "name": "Max",
        "score": 95
    },
    {
        "name": "Bogdan",
        "score": 100
    },
    {
        "name": "Leonid",
        "score": 80
    }]
    
    context = {
        "title": "Results",
        "students": students,
        "test_name" : test_name,
        "max_score" : max_score
    }
    
    return render_template("results.html", **context)
    
    