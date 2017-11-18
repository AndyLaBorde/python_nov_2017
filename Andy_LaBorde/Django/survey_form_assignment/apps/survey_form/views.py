from django.shortcuts import render, redirect

# Create your views here.
def index(request):

  return render(request, 'survey_form/index.html')


def process(request):
	request.session['name'] = request.POST['name']
	request.session['dojoLocation'] = request.POST['dojoLocation']
	request.session['favoriteLanguage'] = request.POST['favoriteLanguage']
	request.session['comments'] = request.POST['comments']


	return redirect('/result')

def result(request):

	return render(request, 'survey_form/result.html')