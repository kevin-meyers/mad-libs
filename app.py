from flask import Flask, render_template, flash, request

import mad_libs


app = Flask(__name__)


@app.route('/')  # This is where the user should select a default story or build one
def home():
	return render_template('home.html')

@app.route('/', methods=['POST'])
def form_post():
	text = request.form['text']
	processed_text = text.upper()
	return processed_text


if __name__ == '__main__':
	app.run()
