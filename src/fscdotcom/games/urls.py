from django.conf.urls import patterns, url

from games import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index',),
		url(r'^(?P<gsid>\d+)/$',views.detail,name='detail'),
	)
