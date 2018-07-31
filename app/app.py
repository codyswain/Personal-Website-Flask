from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")
    
@app.route('/projects')
def projects():
	return render_template("projects.html")

@app.route('/notes')
def notes():
	return render_template("notes.html")

@app.route('/about')
def about():
	return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)