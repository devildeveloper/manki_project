from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

from .models import NewsLetter

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('_replyto')
        response_data = {}

        news = NewsLetter(name=name, email=email)
        news.save()
        
        return redirect('/landing/gracias')
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )