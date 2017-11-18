from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 

# Create your views here.
def index(request):
	request.session['random'] = get_random_string(length=14) 
	if request.session.get('counter') == None:
		request.session['counter'] = 1
	print request.session['random']
	return render(request, 'random_word/index.html')

def process(request):
	request.session['random'] = get_random_string(length=14)
	request.session['counter'] += 1

	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')

