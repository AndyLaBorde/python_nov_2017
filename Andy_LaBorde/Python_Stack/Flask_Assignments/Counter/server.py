from flask import Flask, render_template, session, redirect
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'

def sessionCounter():
	if 'counter' not in session:
		session['counter']=1
	else:
		session['counter']+=1

@app.route('/')
def home():
	sessionCounter() 
	return render_template('index.html')

@app.route('/add2')
def addTwo():
	session['counter']+=1
	return redirect('/')

@app.route('/clear')
def clear():
	session['counter']=0
	return redirect('/')


app.run(debug=True)