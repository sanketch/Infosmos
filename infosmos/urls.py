from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from infosmos.views import home_index
from django.contrib import admin
from User_Profile import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_index, name = 'home_index'),
    url(r'^register/$', include('User_Profile.urls'), name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^dashboard/$', views.user_dashboard, name='dashboard'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    url(r'^thanks/$', 'contact.views.thanks', name='thankyou'),
    url(r'^profile/$', views.user_profile, name='profile'),
    #home page
    # Examples:
    # url(r'^$', 'infosmos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', include('foundation.urls')),#only for testing

    #url(r'^accounts/login/$', 'django_test.views.login'),
    #url(r'^accounts/auth/$', 'django_test.views.auth'),
    #url(r'^accounts/logout/$', 'django_test.views.logout'),
    #url(r'^accounts/loggedin/$, 'django_test.views.loggedin'),
    #url(r'^accounts/invalid$', 'django_test.views.invalid_login'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
#to deploy
