
from oscar.core.loading import get_model, get_class

OfferListView=get_class('offer.views','OfferListView')
RangeDetailView=get_class('offer.views','RangeDetailView')
OfferDetailView=get_class('offer.views','OfferDetailView')

class OfferListView(OfferListView):
    
    template_name = 'yous/offer/list.html'

    
class OfferDetailView(OfferDetailView):
    template_name = 'yous/offer/detail.html'

    
class RangeDetailView(RangeDetailView):
    template_name = 'yous/offer/range.html'

