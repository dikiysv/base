from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Interest(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Adres(models.Model):
	adr = models.CharField(max_length=100)

class Person(models.Model):
	created_by = models.OneToOneField(User)
	adres = models.ManyToManyField(Adres)
	interest = models.ManyToManyField(Interest)