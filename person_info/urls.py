from django.conf.urls import patterns, url

urlpatterns = patterns('',
					# Examples:
					# url(r'^$', 'firstapp.views.home', name='home'),
					# url(r'^blog/', include('blog.urls')),

					url(r'^login/$', 'person_info.views.login'),
					url(r'^logout/$', 'person_info.views.logout'),
					url(r'^register/$', 'person_info.views.register'),
					url(r'^test/', 'person_info.views.test'),
					url(r'^addadres/', 'person_info.views.addadres'),
					url(r'^addvids/', 'person_info.views.addVids'),
					)