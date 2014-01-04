from django.conf.urls import patterns, url

from views import index, article

urlpatterns = patterns('',
    url(r'^$', index, name='home'),
    url(r'^article/(?P<slug>\w+).html$', article, name='article'),
)
