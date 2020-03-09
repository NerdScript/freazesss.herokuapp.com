from . import about
from flask import render_template

@about.route("/about")
def aboutpage():
    return render_template("about.html")