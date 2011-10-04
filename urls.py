from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from ewidencja.admin import larch
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^admin/', include(larch.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )