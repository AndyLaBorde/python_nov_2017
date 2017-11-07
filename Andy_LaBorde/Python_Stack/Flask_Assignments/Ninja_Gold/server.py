from flask import Flask, render_template, redirect, session, request
import datetime
import random
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
	if session.get('gold')==None:
		session['gold'] = 0
	if session.get('activities') == None:
		session['activities']=''
		print session['gold']
	return render_template('index.html')

@app.route('/process_money', methods=['post']) 
def cave():
	if request.form['building'] == 'farm':
		newGold= random.randint(10, 20)
		session['gold'] += newGold
		print newGold
		session['activities'] += "\nEarned {} gold from the Farm!".format(newGold)+' '+str(datetime.datetime.utcnow())
		

	elif request.form['building'] == 'cave':
		newGold= random.randint(5, 10)
		session['gold'] += newGold
		print newGold
		session['activities'] += "\nEarned {} gold from the Cave!".format(newGold)+' '+str(datetime.datetime.utcnow())

	elif request.form['building'] == 'house':
		newGold= random.randint(2, 5)
		session['gold'] += newGold
		print newGold
		session['activities'] += "\nEarned {} gold from the Farm!".format(newGold)+' '+str(datetime.datetime.utcnow())

	elif request.form['building'] == 'casino':
		newGold= random.randint(-50, 50)
		session['gold'] += newGold
		if newGold >=0:
			print 'Earned' +' '+ str(newGold)+' '+ 'gold from the Casino!!!!'
			session['activities'] +=  '\nEarned' +' '+ str(newGold)+' ' + 'gold from the Casino!!!'+' '+str(datetime.datetime.utcnow())
		else:
			print 'Lost ' + str(abs(newGold))+' '+'gold from the Casino... '
			session['activities'] += '\nLost ' +' '+ str(abs(newGold))+' '+ 'gold from the Casino... '+' '+str(datetime.datetime.utcnow())
			session
	return redirect('/')


app.run(debug=True)