from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage(test_variable=None):
	return render_template("homepage.html", test_variable=test_variable)
    # the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    # return """
    # <h1>Hello heroku</h1>
    # <p>It is currently {time}.</p>

    # <img src="http://loremflickr.com/600/400">
    # """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)