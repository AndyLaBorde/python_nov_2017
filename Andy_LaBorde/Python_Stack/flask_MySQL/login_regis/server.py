
from flask import Flask, request, redirect, render_template, session, flash
import re
import md5
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app, 'Login_Registration')

def registration(form_data):
	errors = False

	if len(request.form['fName']) < 1:
		flash('First Name cannot be blank!')
		errors = True

	if len(request.form['lName']) < 1:
		flash('Last Name cannot be blank!')
		errors = True

	if len(request.form['email']) < 1:
		flash('Email cannot be blank!')
		errors = True

	if len(request.form['password']) < 1:
		flash('Password cannot be blank!')
		errors = True

	if len(request.form['passwordC']) < 1:
		flash('Password cannot be blank!')
		errors = True

	if request.form['passwordC'] != request.form['password']:
		flash('Passwords must match!')
		errors = True
	print errors
	return errors

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/process', methods=['POST'])
def register():
	errors = registration(request.form)
	print errors

	if errors == True:
		return redirect('/') 

	else:
		h_pw = md5.new(request.form['password']).hexdigest()

		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
		data = {
			'first_name': request.form['fName'],
			'last_name': request.form['lName'],
			'email': request.form['email'],
			'password': h_pw,
			}

	mysql.query_db(query, data)
	return redirect('/success')

@app.route('/login', methods=['POST'])
def login():

	username = request.form['username']
	password = md5.new(request.form['password']).hexdigest()
	query = "SELECT * FROM users WHERE users.email = :email AND users.password = :password"
	data = { 'email': username, 'password': password}
	user = mysql.query_db(query, data)
	print user
	print data
	
	if user != []:
		return redirect('/success')

	else: 
		flash('OOPS!! Incorrect Username/Password combination!!')
		return redirect('/')

@app.route('/success')
def success():

	return render_template('success.html')

app.run(debug=True)




