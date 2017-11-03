from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Ninjas():
	return render_template('index.html')

@app.route('/ninja')
def Info():
	return render_template('ninja.html')

@app.route('/dojo/new')
def Dojo():
	return render_template('dojos.html')




app.run(debug=True)