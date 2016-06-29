from django.contrib import admin

# Register your models here.
from .models import Schema
from .models import NewsLetter

admin.site.register(Schema)
admin.site.register(NewsLetter)