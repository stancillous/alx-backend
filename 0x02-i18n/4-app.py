#!/usr/bin/env python3
"""
module to force locale with url parameter
"""
from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask(__name__)


class Config(object):
    """class that will configure available languages"""
    LANGUAGES = ["en", "fr"]
    # babel_default_locale = 'en'
    # babel_default_timezone = "UTC"
    BABEL_DEFAULT_LOCALE = 'en'  # Correct attribute name
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Correct attribute name

app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def home_page():
    """func to serve the home route"""
    return render_template("4-index.html")

@babel.localeselector
def get_locale():
    """determines the best match with our
    supported languages"""
    locale_value = request.args.get("locale")
    if locale_value in app.config['LANGUAGES']:
        # print("present ", locale_value)
        return locale_value
    # print("lang is ", request.accept_languages.best_match(app.config['LANGUAGES']))
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)