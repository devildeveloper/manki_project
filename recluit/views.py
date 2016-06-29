from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

from .models import Schema

# Create your views here.
def recluit(request):
    if request.method == 'POST':
        experience_about = request.POST.get('desc')
        experience_type  = request.POST.get('about')
        recluit_motive   = request.POST.get('motive')
        recluit_name     = request.POST.get('name')
        recluit_email    = request.POST.get('mail')
        recluit_phone    = request.POST.get('phone')

        response_data = {}

        schema = Schema(experience_type=experience_type,experience_about=experience_about,recluit_motive=recluit_motive,recluit_name=recluit_name,recluit_email=recluit_email,recluit_phone=recluit_phone)
        schema.save()
        
        return redirect('/landing/gracias')
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )