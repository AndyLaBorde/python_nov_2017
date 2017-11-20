from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
	name = models.CharField(max_length=225)
	city = models.CharField(max_length=225)
	state = models.CharField(max_length=2)

class Ninja(models.Model):
	first_name = models.CharField(max_length=225)
	last_name = models.CharField(max_length=225)
	dojo = models.ForeignKey(Dojo, related_name="ninjas")

	def __unicode__(self):
		return "id: " + str(self.id) +",first_name: " + self.first_name + ",last_name: " + self.last_name + ",Dojo: " + str(self.dojo.id)