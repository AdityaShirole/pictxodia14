from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.contrib import admin, staticfiles
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'XOdia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bots/', include('bots.urls')),
    (r'^$', RedirectView.as_view(url = '/bots/')),
    (r'^description/$', TemplateView.as_view(template_name = 'description.html')),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
