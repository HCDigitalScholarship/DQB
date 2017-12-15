from django import forms
from django.forms import ModelForm
from django.db import models
from dqb_app.models import *
from models import Person

class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = '__all__'


#class AuthorForm(ModelForm):
 #   class Meta:
  #      model = Author
   #     fields = '__all__'


#class PersonForm(forms.Form):
#    last_name = forms.CharField(label='Last Name', max_length=100)
#	first_name = forms.CharField("First Name", max_length=100, blank = True)
#	birth_date = forms.CharField("Birth Date", max_length=20, blank = True)
#	death_date =  forms.CharField("Death Date", max_length=20, blank = True)
#	locations = forms.TextField("Location", blank = True)
#	references = forms.TextField("Reference", blank = True)
#	textfile = forms.TextField("Text", blank = True, null = True)    
    