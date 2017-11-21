from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return 'id: ' +str(self.id)+',name: ' + self.name

class Authors(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	notes = models.TextField()
	books = models.ManyToManyField(Book, related_name="authors")

	def __unicode__(self):
		return 'id: ' +str(self.id)+',first_name: ' + self.first_name +', last_name: ' + self.last_name + ',email :' + self.email + ',notes :' + self.notes