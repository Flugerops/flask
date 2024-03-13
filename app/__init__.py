from flask import Flask


app = Flask(__name__)
app.template_folder = "../templates/"

from . import routes


if __name__ == "__main__":
    app.run(port=8000)