from flask import Flask, render_template, flash, request

import mad_libs

text = open('data/example.txt').read()
tags = []

app = Flask(__name__)
app.debug=True

@app.route('/')  # This is where the user should select a default story or build one
def choice():
	return render_template('choice.html')

@app.route('/input')
def user_story():
	return render_template('input.html')

@app.route('/form')
@app.route('/form', methods=['POST'])
def form():
	if request.method == 'POST':
		global text
		text = request.form.get('input')
	global tags
	tags = mad_libs.get_tags(text)
	
	return render_template('form.html', questions=mad_libs.make_questions(tags))


@app.route('/story', methods=['POST'])
def handle_data():
	user_in = {tag: request.form.getlist(tag) for tag in request.form}
	story = mad_libs.build_story(text, tags, user_in)
	
	return render_template('story.html', text=story)


if __name__ == '__main__':
	app.run()
