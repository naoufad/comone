from django.conf.urls import url
from contact.views import ContactView
from . import views 
app_name='contact'

urlpatterns = [
    url(r'^$',ContactView.as_view(), name='contact'),
    url(r'^facebook/',views.facebookView, name='facebook'),
]
