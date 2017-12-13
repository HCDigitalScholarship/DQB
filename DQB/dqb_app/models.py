from django.db import models

class Person(models.Model):
	
	id = models.IntegerField("Person ID", primary_key=True)
	#other_filename = models.CharField("Associated File", max_length = 100, blank = True) #This would be if there were a second page this person is associated with.
	last_name = models.CharField("Last Name", max_length=100, blank = True)
	first_name = models.CharField("First Name", max_length=100, blank = True)
	birth_date = models.CharField("Birth Date", max_length=20, blank = True)
	death_date =  models.CharField("Death Date", max_length=20, blank = True)
	#locations = models.TextField("Locations", blank = True)
	locations = models.ManyToManyField("Location", blank = True)
	#references = models.TextField("References", blank = True)
	references = models.ManyToManyField("Reference", blank = True)
	textfile = models.ForeignKey("Text", blank = True, null = True)
	#will want to include file and updated text
	
	def __unicode__(self):
		return str(self.id) + " " + self.last_name # etc.
		
class Text(models.Model):
	filename = models.CharField("Image File", max_length = 100)
	text = models.TextField("Revised Text", blank = True)
	
	def __unicode__(self):
		return self.filename + " " + self.text
		
class Organization(models.Model):
	orgName = models.CharField("Organization Name", max_length = 100)
	
	def __unicode__(self):
		return self.orgName
		
class Location(models.Model):
	placeName = models.CharField("Location", max_length = 100)
	
	def __unicode__(self):
		return self.placeName
		
class Reference(models.Model):
	ref = models.TextField("Reference")
	
	def __unicode__(self):
		return self.ref