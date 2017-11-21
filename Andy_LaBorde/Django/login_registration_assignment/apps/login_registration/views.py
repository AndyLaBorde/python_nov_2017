from django.shortcuts import render, redirect
from .models import Users
# Create your views here.
def index(request):
	if request.session.get('errors') == None:
		request.session['errors'] = []
	return render(request, 'login_registration/index.html')

def register(request):
	if request.method == 'POST':
		errors = Users.objects.register_validation(request.POST)
		print errors
	if len(errors) != 0:
		request.session['errors'] = errors
		return redirect('/')
	else: 
		user = Users.objects.register(request.POST)
		request.session['user_id'] = user.id
		return redirect('/success')	
		print Users.objects.all()

def login(request):
	errors = Users.objects.login_validation(request.POST)
	if len(errors) != 0:
		request.session['errors'] = errors
		return redirect('/')
	else:
		user= Users.objects.login(request.POST)
	request.session['user_id'] = user.id
	request.session['name'] = user.first_name
	return redirect('/success')

def success(request):



	return render(request, 'login_registration/success.html')