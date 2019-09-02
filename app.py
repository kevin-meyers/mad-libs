from flask import Flask, render_template, flash, request

import mad_libs


app = Flask(__name__)
app.debug=True

@app.route('/')  # This is where the user should select a default story or build one
def choice():
	return render_template('choice.html')

@app.route('/form')
def form():
	return render_template('form.html', questions=mad_libs.default_questions())

@app.route('/form', methods=['POST'])
def handle_data():
	user_in = request.form.get('placeholder')
	return user_in.upper()


if __name__ == '__main__':
	app.run()
