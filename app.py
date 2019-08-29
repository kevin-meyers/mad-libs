from flask import Flask

from mad_libs import MadLibs


m = MadLibs(open('example.txt').read())


app = Flask(__name__)


@app.route('/')
def test():
	return m.run()


