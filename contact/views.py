from django.views.generic import  TemplateView
from django.shortcuts import redirect


def facebookView(request):
    
    return redirect('https://www.facebook.com/comoresEnLigne/')

class ContactView(TemplateView):
    template_name='yous/contact/contact_home.html'


class Partenaires(TemplateView):
    template_name='yous/contact/partenaires.html'

class Services(TemplateView):
    template_name='yous/contact/services.html'


class MentionsLegales(TemplateView):
    template_name='yous/contact/mentions_legales.html'


class cg(TemplateView):
    template_name='yous/contact/conditions_generales.html'


class Nous(TemplateView):
    template_name='yous/contact/nous.html'


class Batiment(TemplateView):
    template_name='yous/contact/batiment.html'


class Allimentation(TemplateView):
    template_name='yous/contact/allimentation.html'



class Riz(TemplateView):
    template_name='yous/contact/riz.html'



    
