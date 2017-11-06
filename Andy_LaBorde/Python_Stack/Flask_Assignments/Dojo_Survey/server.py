from flask import Flask, render_template, redirect, request, session, flash
app= Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def Form():
	return render_template('index.html')

# @app.route('/return', methods=['POST'])
# def Submit():
# 	print "form"
# 	return redirect('/result')

@app.route('/result', methods=['POST'])
def Result():
	if len(request.form['name']) < 1:
		flash("Name Cannot be EMPTY!!")
	if len(request.form['comments']) <1:
		flash("Comment can not be empty")
	else:
		flash("Success! your name is {}".format(request.form['name']))
		# return redirect('/')

	return render_template('result.html', name=request.form['name'], location=request.form['dojoLocation'], language=request.form['favoriteLanguage'], comment=request.form['comments'] )


app.run(debug=True)