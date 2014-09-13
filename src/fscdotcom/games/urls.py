from django.conf.urls import patterns, url

from games import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index',),
        url(r'^(?P<year>\d+)/(?P<season_type>\Regular|Preseason|Postseason)/(?P<week>\d+)/$', views.index, name='index',),
        url(r'^(?P<gsid>\d+)/$',views.detail, name='detail'),
        )
