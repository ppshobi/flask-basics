from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Shobi"):
	return "Hello {}".format(name)

app.run(debug=True, port=8000)