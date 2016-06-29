# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone as django_tz

from django.db import models

# Create your models here.
class Schema(models.Model):
#    motive = models.ForeignKey(Question, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=2,help_text="can be Explorar,Enseñar,Entretener")
    experience_type = models.CharField(max_length=100,help_text="what kind of experience would you like to guide.")
    experience_about= models.CharField(max_length=200,help_text="what about the experience ?")
    recluit_motive = models.CharField(max_length=200,help_text="motive to be part of manki")
    recluit_name   = models.CharField(max_length=200,help_text="your name")
    recluit_email  = models.EmailField(max_length=100,help_text="your email")
    recluit_phone  = models.CharField(max_length=20,help_text="your phone")
    createdAt      = models.DateTimeField(default=django_tz.now, blank=True)