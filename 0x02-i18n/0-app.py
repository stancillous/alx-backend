#!/usr/bin/env python3
"""module to serve a home route in flask"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home_page():
    """func to serve the home route"""
    return render_template("0-index.html")

app.run(debug=True)