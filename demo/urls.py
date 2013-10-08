from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from ipmanager import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', views.home, name='home'),
    url(r'^hosts/$', views.HostList.as_view(), name='list'),
    url(r'^hosts/(?P<pk>[0-9]+)/$', views.HostList.as_view(), name='update'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns = format_suffix_patterns(urlpatterns)
