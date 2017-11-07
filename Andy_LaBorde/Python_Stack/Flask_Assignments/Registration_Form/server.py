from flask import Flask, redirect, render_template, flash, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():


	if len(request.form['email']) < 1:
		flash('* Email cannot be blank! *', "email")
	elif not EMAIL_REGEX.match(request.form['email']):	
		flash('* Invalid Email Address!! *', "email")

	if len(request.form['fName']) < 1:
		flash('* You need a First Name *', "fName")
	elif request.form['fName'].isalpha()== False:		
		flash('* Names cannot contain numbers! *', "fName")

	if len(request.form['lName']) < 1:
		flash('* You need a Last Name *', "lName")
	elif request.form['lName'].isalpha()== False:		
		flash('* Names cannot contain numbers! *', "lName")


	if len(request.form['password']) < 8:
		flash('* Password must be over 8 characters! *', 'password')


	if request.form['password_comp'] != request.form['password']:
		flash('* Passwords Do Not Match! *', "password_comp")


	return redirect('/')

app.run(debug=True)