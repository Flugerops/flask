from flask import Flask


app = Flask(__name__)
app.template_folder = "../templates/"

from . import routes


