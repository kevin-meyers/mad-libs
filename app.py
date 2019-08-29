from flask import Flask, render_template, flash, request


from mad_libs import MadLibs


m = MadLibs(open('example.txt').read())


app = Flask(__name__)


@app.route('/')
def form():
	return render_template('form.html')

@app.route('/', methods=['POST'])
def form_post():
	text = request.form['text']
	processed_text = text.upper()
	return processed_text


if __name__ == '__main__':
	app.run()
