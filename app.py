from flask import Flask, render_template, flash, request

import mad_libs

text = open('data/example.txt').read()

app = Flask(__name__)
app.debug=True

@app.route('/')  # This is where the user should select a default story or build one
def choice():
	return render_template('choice.html')

@app.route('/input')
def user_story():
	return render_template('user_input.html')


@app.route('/form', methods=['POST'])
def form():
	if request.method == 'POST':
		return request.form.to_dict()
	return render_template('form.html', questions=mad_libs.default_questions(text))


@app.route('/story', methods=['POST'])
def handle_data():
	user_in = {tag: request.form.getlist(tag) for tag in request.form}

	return mad_libs.build_story(text, user_in.keys(), user_in)


if __name__ == '__main__':
	app.run()
