from django.views.generic import  TemplateView
from django.shortcuts import redirect


def facebookView(request):
    
    return redirect('https://www.facebook.com/comoresEnLigne/')

class ContactView(TemplateView):
    template_name='yous/contact/contact_home.html'



