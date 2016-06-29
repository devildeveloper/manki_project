from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^landing/subscribe/$', views.subscribe, name='subscribe'),
]