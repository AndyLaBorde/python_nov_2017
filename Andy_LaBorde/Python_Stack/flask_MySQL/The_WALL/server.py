
from flask import Flask, request, redirect, render_template, session, flash
import re
import md5
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app, 'wall')

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
	return redirect('/')

@app.route('/login', methods=['POST'])
def login():

	username = request.form['username']
	password = md5.new(request.form['password']).hexdigest()
	query = "SELECT * FROM users WHERE users.email = :email AND users.password = :password"
	data = { 'email': username, 'password': password }
	user = mysql.query_db(query, data)
	
	print user
	
	
	if user != []:
		session['name'] = user[0]['first_name']
		session['users_id'] = user[0]['id']
		print 'fuck off' + session['name'] + str(session['users_id'])
		return redirect('/wall')

	else: 
		flash('OOPS!! Incorrect Username/Password combination!!')
		return redirect('/')

@app.route('/wall')
def success():
	query = "SELECT messages.id as message_id, users.first_name, messages.message,  messages.created_at, messages.users_id FROM messages JOIN users ON users.id = messages.users_id"
	messages = mysql.query_db(query)
	data ={}
	
	queryC = "SELECT comments.comment, users.first_name, comments.created_at, comments.messages_id FROM comments JOIN users ON users.id = comments.users_id;"
	comments = mysql.query_db(queryC)
	print messages

	for i in messages:
		for j in comments:
			if j['messages_id'] == i['message_id']:
				print j
	return render_template('wall.html', messages = messages, data = data, comments= comments)

@app.route('/message', methods=['POST'])
def message():
	print session['users_id']
	query = "INSERT INTO messages (users_id, message, created_at, updated_at) VALUES (:users_id, :message, NOW(), NOW())"
	data = {
			'users_id': int(session['users_id']),
			'message': request.form['message'],
			}
	mysql.query_db(query, data)
	
	
	return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
	
	comment = request.form['comment']
	messages_id = request.form['comment_m']
	print "hello" + messages_id 
	print session['users_id']
	query = "INSERT INTO comments (users_id, comment, created_at, updated_at, messages_id) VALUES (:users_id, :comment, NOW(), NOW(), :messages_id)"
	data = {
			'messages_id': messages_id,
			'users_id': int(session['users_id']),
			'comment': request.form['comment'],

			}
	mysql.query_db(query, data)
	return redirect('/wall')

app.run(debug=True)




