from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
#    template = loader.get_template('landing/index.html')
#    return HttpResponse(template.render(request))
    return render(request,'landing/index.html') 
def gracias(request):
    template = loader.get_template('landing/gracias.html')
    return HttpResponse(template.render(request)) 
def guias(request):
    return render(request,'landing/guias.html') 
def guias_out(request):
    template = loader.get_template('landing/guias-out.html')
    return HttpResponse(template.render(request)) 
def landing_out(request):
    template = loader.get_template('landing/landing-out.html')
    return HttpResponse(template.render(request))
def viajeros(request):
    return render(request,'landing/viajeros.html')