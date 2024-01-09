#!/usr/bin/env python3
"""
module to try and get user locale from request
"""
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """class that will configure available languages"""
    LANGUAGES = ["en", "fr"]
    babel_default_locale = "en"
    babel_default_timezone = "UTC"

app.config.from_object(Config())

def get_locale():
    """determines the best match with our
    supported languages"""

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/", strict_slashes=False)
def home_page():
    """func to serve the home route"""
    return render_template("3-index.html")


babel.localeselector(get_locale)

if __name__ == "__main__":
    app.run(debug=True)