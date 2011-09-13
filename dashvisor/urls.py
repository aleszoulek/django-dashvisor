from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dashvisor.views',
    url(r'^$', 'dashboard', name='dashboard'),
)

