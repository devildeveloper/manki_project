from __future__ import unicode_literals

from django.db import models
from django.utils import timezone as django_tz

import random
import string
# Create your models here.

class Schema(models.Model):
    # generate random function    
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    name      = models.CharField(max_length=200,help_text="Your Name")
    lastName  = models.CharField(max_length=200,help_text="Your Lastname")
    email     = models.EmailField(max_length=200,help_text="Your Email")
    passwd    = models.CharField(max_length=12,default=id_generator())
    createdAt = models.DateTimeField(default=django_tz.now, blank=True)