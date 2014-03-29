from django.conf.urls import patterns, url
from User_Profile import views

urlpatterns = patterns('',
    url(r'^$', views.register, name='register'),)
