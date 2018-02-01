from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from oscar.apps.checkout import views
from oscar.apps.payment import forms, models
from oscar.core.loading import get_class
from paypal.payflow import facade

PaymentDetailsView=get_class('checkout.views','PaymentDetailsView')
ShippingAddressView=get_class('checkout.views','ShippingAddressView')

class ShippingAddressView(ShippingAddressView):
     template_name = 'yous/checkout/shipping_address.html'


class PaymentDetailsView(PaymentDetailsView):
    
    template_name = 'yous/checkout/payment_details.html'
