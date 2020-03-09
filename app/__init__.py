from flask import Flask, Blueprint, render_template
from app.home import home
from app.about import about

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(about)

@app.errorhandler(404)
def not_foundpage(e):
	return render_template('404.html'), 404