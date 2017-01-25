from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Shobi"):
	return "Hello {}".format(name)

@app.route('/add/<num1>/<num2>')
def add(num1,num2):
	return "{} + {} = {}".format(num1,num2,int(num1)+int(num2))

app.run(debug=True, port=8000)