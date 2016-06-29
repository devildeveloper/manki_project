from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^landing/gracias/$', views.gracias, name='gracias'),
    url(r'^landing/guias/$', views.guias, name='guias'),
    url(r'^landing/guias-out/$', views.guias_out, name='guias_out'),
    url(r'^landing/landing-out/$', views.landing_out, name='landing_out'),
    url(r'^landing/viajeros/$', views.viajeros, name='viajeros'),
]