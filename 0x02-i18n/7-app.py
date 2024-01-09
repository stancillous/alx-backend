#!/usr/bin/env python3
"""
module to force locale with url parameter
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, _
from pytz import UnknownTimeZoneError, timezone

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
    logged_in = True if g.user else False

    return render_template("7-index.html", logged_in=logged_in)

@babel.localeselector
def get_locale():
    """determines the best match with our
    supported languages"""

    # get locale from URL parameters
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale

    # get locale from user settings
    if g.user:
        locale = g.user.get("locale")
        if locale in app.config['LANGUAGES']:
            return locale

    # get locale from request header
    locale = request.headers.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale

    # use default user's locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """get user's timezone"""
    # get locale from URL parameters
    timezone = request.args.get("timezone")
    try:
        return timezone.zone
    except UnknownTimeZoneError:
        print("unknown timezone") 

    # get timezone from user settings
    if g.user:
            try:
                timezone = g.user.get("timezone")
                return timezone.zone
            except UnknownTimeZoneError:
                print("unknown timezone") 
    
    return "UTC"

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """return dict or None if user ID cannot be found"""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))


@app.before_request
def before_request():
    """func to be called before every request"""
    user = get_user()
    # print("\t\t user is ", user)
    g.user = user

if __name__ == "__main__":
    app.run(debug=True)