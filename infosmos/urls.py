from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from infosmos.views import home_index
from django.contrib import admin
from User_Profile import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_index, name = 'home_index'),
    url(r'^matches/$', 'Matches.views.matches', name='dashboard'),

    url(r'^messages/', include('django_messages.urls'), name='messages'),
    url(r'^chats/', include('chat.urls')),
    url(r'^register/$', include('User_Profile.urls'), name='register'),
    url(r'^buddy/$', views.buddy, name='buddy'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^dashboard/$', views.user_dashboard, name='dashboard'),
    url(r'^accounts/signup/$', include('User_Profile.urls'), name='register'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    url(r'^thanks/$', 'contact.views.thanks', name='thankyou'),
    url(r'^profile/$', views.user_profile, name='profile'),
    url(r'^accounts/profile/$', views.user_profile, name='profile'),

    url(r'^accounts/', include('allauth.urls')),
    #url(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
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
