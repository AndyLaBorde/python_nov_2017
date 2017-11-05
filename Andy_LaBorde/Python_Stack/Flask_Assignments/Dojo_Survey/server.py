from flask import Flask, render_template, redirect
app= Flask(__name__)

@app.route('/')
def Form():
	return render_template('index.html')

# @app.route('/return', methods=['POST'])
# def Submit():
# 	print "form"
# 	return redirect('/result')

@app.route('/result', methods=['POST'])
def Result():
	print "form info"
	return render_template('result.html')


app.run(debug=True)