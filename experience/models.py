from __future__ import unicode_literals

from django.db import models

from guide.models import Schema as Guide

class Experience_Dates(models.Model):
    date   = models.DateTimeField() 
# Create your models here.
class Schema(models.Model):
    name   = models.CharField(max_length=200,help_text="Experience name")
    city   = models.CharField(max_length=200,help_text="city")
    detail = models.CharField(max_length=200,help_text="experience details")
    conditions=models.CharField(max_length=200,help_text="conditions to take experience")
    dates  = models.ForeignKey(Experience_Dates,on_delete=models.CASCADE)
    guide  = models.OneToOneField(Guide, on_delete=models.CASCADE)
    price  = models.DecimalField(help_text="princing",max_digits=5,decimal_places=2)