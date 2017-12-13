from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from models import Person

#from pymongo import MongoClient

#client = MongoClient()
#db = client['dqb_database']
#collection = db['dqb_collection']

def home(request):
	return render(request, 'home.html')
	
def profile(request, person_id):
	#document = collection.find_one({'file' : 'DQB_ECCLES-EDRIDGE_Page_080.jpg.jpg'})
	#context = {'person_id': person_id, 'document': document}
	context = {'person_id':person_id}
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
    
    
    

"""