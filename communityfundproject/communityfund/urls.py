from django.conf.urls import patterns, url
from communityfund import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^projects/$', views.projects, name='projects'),
        url(r'^topprojects/$', views.topprojects, name='topprojects'),
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^home/$', views.home, name='home'),
        url(r'^createproject/$', views.createproject, name='createproject'),
        url(r'^intro/$', views.intro, name='intro'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^about/$', views.about, name='about'),
        url(r'^find/$', views.find, name='find'),
        url(r'^editprofile/$', views.editprofile, name='editprofile'),
        url(r'^profile/(?P<profile_name>[\w\-]+)/$', views.profile, name='profile'),
        url(r'^projects/(?P<project_name>[\w\-]+)/$', views.projects, name='projects'),
        url(r'^payment/(?P<project_name>[\w\-]+)/$', views.payment, name='payment'),
        url(r'^settings/$', views.settings, name='settings'))
