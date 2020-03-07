from . import home
from flask import render_template

@home.route("/")
def homepage():
	return render_template('home.html')