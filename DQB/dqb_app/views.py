from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from models import Person
from .forms import PersonForm

#from pymongo import MongoClient

#client = MongoClient()
#db = client['dqb_database']
#collection = db['dqb_collection']

def home(request):
	return render(request, 'home.html')
	
def profile(request, person_id):
	#document = collection.find_one({'file' : 'DQB_ECCLES-EDRIDGE_Page_080.jpg.jpg'})
	#context = {'person_id': person_id, 'document': document}
	### from django docs:
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'home.html')
	else:	
		form = PersonForm()
	context = {'person_id':person_id, 'form':form}
	return render(request, 'profile.html', context)
	
	
	
def profile_index(request):
	index = []
	for i in range(0, 10):
		index.append(i)
	context = {'index':index}
	return render(request, 'profile_index.html', context)
	

	
"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})  
    

"""