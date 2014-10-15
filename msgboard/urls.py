from django.conf.urls import include, url
from msgboard import views

urlpatterns = [
	# login action
	url(r'^loginform/$', views.loginform, name='loginform'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	
	# user registration
	url(r'^register/$', views.register, name='register'),
	url(r'^registerform/$', views.registerform, name='registerform'),

	# message board home
    url(r'^$', views.index, name='index'),
    
    # page for a particular topic
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.topic, name='topic'),
     
    # creating a new topic
    url(r'^newtopic/$', views.newtopic, name='newtopic'),
    url(r'^newtopicform/$', views.newtopicform, name='newtopicform'),
    
    # creating a new message for a particular topic
    url(r'^topic/(?P<topic_id>[0-9]+)/newmsg/$', views.newmsg, name='newmsg'),
    url(r'^topic/(?P<topic_id>[0-9]+)/newmsgform/$', views.newmsgform, name='newmsgform')
]
