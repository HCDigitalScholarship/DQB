from django.db import models

class Person(models.Model):
	
	person_id = models.CharField("Person ID", max_length = 50)
	filename = models.CharField("File Name", max_length = 100)
	other_filename = models.CharField("Associated File", max_length = 100, blank = True) #This would be if there were a second page this person is associated with.
	last_name = models.CharField("Last Name", max_length=100, blank = True)
	first_name = models.CharField("First Name", max_length=100, blank = True)
	birth_date = models.CharField("Birth Date", max_length=20, blank = True)
	death_date =  models.CharField("Death Date", max_length=20, blank = True)
	locations = models.TextField("Locations", blank = True)
	bio_info = models.TextField("Biographical Information", blank = True)
	references = models.TextField("References", blank = True)
	
	def __unicode__(self):
		return self.id + " " + self.filename  + " " + self.other_filename # etc.