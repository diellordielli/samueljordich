from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import redirect

from feincms.translations import short_language_code


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Home
    url(r'^$', 'ruediwidmerch.views.home', name='home'),

    # Grafik
    url(r'^grafik/$', 'ruediwidmerch.views.grafik', name='grafik'),

    # News
    url(r'^aktuell/$', 'ruediwidmerch.views.news', name='news'),

    # News Year
    url(r'^aktuell/(?P<year>\d{4})/$', 'ruediwidmerch.views.newsyear', name='newsyear'),

    # Portrait
    url(r'^portrait/$', 'ruediwidmerch.views.portrait', name='portrait'),

    # Kontakt
    url(r'^contact/$', 'ruediwidmerch.views.contact', name='contact'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^upload/(.*)', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )
