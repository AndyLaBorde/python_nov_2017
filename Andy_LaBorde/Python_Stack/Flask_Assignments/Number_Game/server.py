from flask import Flask, render_template, redirect, session, request
import random

app=Flask(__name__)
app.secret_key='ThisIsSecret'

@app.route('/')
def home():
	if session.get('num') == None:
		session['num']=random.randint(1, 100)
	return render_template('index.html')


@app.route('/submit', methods=['post'])
def answer():
	if int(request.form['guess']) > session['num']:
		result = "TOO HIGH!!"
		return render_template('index.html', result=result)
	elif int(request.form['guess']) < session['num']:
		result = "too low.."
		return render_template('index.html', result=result)
	else:
		result = "Perfect! the number is {}".format(session['num'])
		return render_template('index.html', result=result)	
	print session['num']
	print request.form['guess']
	return redirect('/')
@app.route('/again')
def again():
	return redirect('/')
app.run(debug=True)
