from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/friends', methods=['POST'])
def create():
    friends + mysql.query_db('SELECT * FROM friends')
    return redirect('index.html')
app.run(debug=True)
