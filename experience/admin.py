from django.contrib import admin

# Register your models here.
from .models import Schema
from .models import Experience_Dates

admin.site.register(Schema)
admin.site.register(Experience_Dates)