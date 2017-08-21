from django.conf.urls import patterns, include, url
from django.contrib import admin
import person_info.urls
urlpatterns = [
	# Examples:
	# url(r'^$', 'musthave.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^auth/', include(person_info.urls)),
##	url(r'^', 'registration.views.test'),	

]
