from flask import Flask, request, redirect, render_template, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'Email_val')
@app.route('/')
def index():
	query = "SELECT * FROM email"                           
	friends = mysql.query_db(query)               
	print friends            
	return render_template('index.html')



@app.route('/process', methods=['POST'])
def create():
	if len(request.form['email']) < 1:
		flash('email cannot be BLANK!')
	elif EMAIL_REGEX.match(request.form['email']): 
		query = "INSERT INTO email (email) VALUES (:email)"
		data= { 
		'email': request.form['email'] 
		}
		mysql.query_db(query, data)
		return redirect('/success')
	else:
		flash('you don fucked up A-ARON')
		return redirect('/')

@app.rout('/success')
def success():
	return render_template('success.html', email= session['email'], all_emails= )
app.run(debug=True)