from django.conf.urls import patterns, url

from okr import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),	
	url(r'^archived/$', views.archived, name='archived'),	
)