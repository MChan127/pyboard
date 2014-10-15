from django.conf.urls import include, url
from django.contrib import admin
from msgboard import views

urlpatterns = [
	# admin interface
    url(r'^admin/', include(admin.site.urls)), 
    # message board views
    url('', include('msgboard.urls')),
    # restricted page
    url(r'^restricted/$', views.restricted, name='restricted')
]
