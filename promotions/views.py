from oscar.core.loading import get_class

HomeView = get_class('promotions.views', 'HomeView')

class HomeView(HomeView):
    template_name = "yous/promotions/accueil.html"
   
