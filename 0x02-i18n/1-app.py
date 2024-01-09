#!/usr/bin/env python3
"""
module for a simple Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """class that will configure available languages"""
    LANGUAGES = ["en", "fr"]
    babel_default_locale = "en"
    babel_default_timezone = "UTC"

app.config.from_object(Config())

@app.route("/", strict_slashes=False)
def home_page():
    """func to serve the home route"""
    return render_template("1-index.html")

app.run(debug=True)
