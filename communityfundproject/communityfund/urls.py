from django.conf.urls import patterns, url
from communityfund import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^projects/$', views.projects, name='projects'),
        url(r'^topprojects/$', views.topprojects, name='topprojects'),
        url(r'^create/$', views.create, name='create'),
        url(r'^intro/$', views.intro, name='intro'),
        url(r'^createdetail/$', views.createdetail, name='createdetail'),
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^home/$', views.home, name='home'),
        url(r'^createproject/$', views.createproject, name='createproject'),
        url(r'^intro/$', views.intro, name='intro'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^about/$', views.about, name='about'))
