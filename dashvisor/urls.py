from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dashvisor.views',
    url(r'^$', 'dashboard', name='dashvisor_dashboard'),
    url(r'^control/(?P<server>[a-z0-9\.]+)/(?P<process>[a-z:_-]+)/(?P<action>[a-z]+)/$', 'control', name='dashvisor_control'),
    url(r'^query/$', 'query', name='dashvisor_query'),
)

