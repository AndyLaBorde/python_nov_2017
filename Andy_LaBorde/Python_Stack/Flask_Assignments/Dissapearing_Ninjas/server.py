from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/ninja')
def Ninjas():
	return render_template('ninja.html')


@app.route('/ninja/red')
def Red():
	return render_template('red.html')

@app.route('/ninja/blue')
def Blue():
	return render_template('blue.html')

@app.route('/ninja/purple')
def Purple():
	return render_template('purp.html')

@app.route('/ninja/orange')
def Orange():
	return render_template('oran.html')\

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")


app.run(debug=True)