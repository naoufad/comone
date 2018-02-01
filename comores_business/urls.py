
############### comores_business URL Configuration ##################



from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps import views
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from oscar.app import application
from oscar.views import handler403, handler404, handler500
#from search.sitemaps import base_sitemaps
from paypal.payflow.dashboard.app import application as payflow
from paypal.express.dashboard.app import application as express_dashboard


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),
    url(r'^contact/',include('contact.urls')),
]


urlpatterns += i18n_patterns(
    # PayPal Express integration...
    url(r'^checkout/paypal/', include('paypal.express.urls')),
    # Dashboard views for Payflow Pro
    url(r'^dashboard/paypal/payflow/', include(payflow.urls)),
    # Dashboard views for Express
    url(r'^dashboard/paypal/express/', include(express_dashboard.urls)),

)

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
