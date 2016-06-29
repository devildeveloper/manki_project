from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^recluit/join$', views.recluit, name='join'),
]