from django.conf.urls import patterns, url
from communityfund import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.login, name='login'),
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^about/$', views.about, name='about'))
