from django.conf.urls import patterns, url
from frontend import views


urlpatterns = patterns(
		'',
		url(r'^$',views.index, name = 'index'),
		url(r'about/', views.about, name = 'about'),
		url(r'^add_profile/$', views.add_profile, name='add_profile'),
		url(r'^register/$', views.register, name = 'register'),
		url(r'^login/$', views.user_login, name ='login'),
		url(r'^restricted/', views.restricted, name='restricted'),
		url(r'^logout/$', views.user_logout, name='logout'),
	)

