from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	request.session['allInfo'] = None
	return render(request, 'session_words/index.html')

def process(request):
	request.session['word'] = request.POST['word']
	request.session['color'] = request.POST['color']
	request.session['size'] = request.POST['size']

	print request.session['word']
	

	if request.session.get(allInfo) == None:
		request.session['allInfo'] = []

	if request.POST['size'] == None:
		request.session['size'] = '14px'
	return redirect('/')

def clear(request):

	request.session['allInfo'] = None

	return redirect('/')