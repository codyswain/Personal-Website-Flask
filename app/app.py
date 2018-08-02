from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
# app = Flask(__name__, static_url_path='/static')

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


''' Here are the note pages '''
@app.route('/notes_schedule')
def notes_schedule():
	return render_template("notes_schedule.html")

@app.route('/notes_big_o_notation')
def notes_big_o_notation():
	return render_template("notes_big_o_notation.html")

@app.route('/notes_algorithms_from_scratch1')
def notes_algorithms_from_scratch1():
	return render_template("notes_algorithms_from_scratch1.html")

@app.route('/notes_algorithms_from_scratch2')
def notes_algorithms_from_scratch2():
	return render_template("notes_algorithms_from_scratch2.html")

@app.route('/notes_algorithms_from_scratch3')
def notes_algorithms_from_scratch3():
	return render_template("notes_algorithms_from_scratch3.html")

@app.route('/notes_algorithms_from_scratch4')
def notes_algorithms_from_scratch4():
	return render_template("notes_algorithms_from_scratch4.html")

@app.route('/notes_algorithms_from_scratch5')
def notes_algorithms_from_scratch5():
	return render_template("notes_algorithms_from_scratch5.html")

@app.route('/notes_mistakes_list')
def notes_mistakes_list():
	return render_template("notes_mistakes_list.html")

@app.route('/notes_company_applications_list')
def notes_company_applications_list():
	return render_template("notes_company_applications_list.html")


''' Project pages '''
@app.route('/projects_3d_printer')
def projects_3d_printer():
	return render_template("projects_3d_printer.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)