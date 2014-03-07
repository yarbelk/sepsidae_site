from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import contribs.urls
import sepsid.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(contribs.urls)),
    url(r'^api/', include(sepsid.urls)),
)
