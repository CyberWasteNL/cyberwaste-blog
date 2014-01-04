from django.conf.urls import patterns, url

from views import index, article

urlpatterns = patterns('',
    url(r'^article/(?P<slug>.+).html$', article),
    url(r'^$', index, name='home'),
)
