from flask import Flask, render_template, redirect
app= Flask(__name__)

# class Form():
# 	name = Textfield('name:')

@app.route('/')
def Name():
	
	return render_template('index.html')

@app.route('/register', methods=['POST'] )
def Submit():
	print "inside resgister"
	return redirect('/')


app.run(debug=True)