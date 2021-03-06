from decimal import Decimal as D
from order.models import ShippingAddress
from django.utils.translation import ugettext_lazy as _

from oscar.core import prices


class Base(object):
    """
    Shipping method interface class

    This is the superclass to the classes in methods.py, and a de-facto
    superclass to the classes in models.py. This allows using all
    shipping methods interchangeably (aka polymorphism).

    The interface is all properties.
    """

    #: Used to store this method in the session.  Each shipping method should
    #  have a unique code.
    code = '__default__'

    #: The name of the shipping method, shown to the customer during checkout
    name = 'Default shipping'

    #: A more detailed description of the shipping method shown to the customer
    #  during checkout.  Can contain HTML.
    description = ""

    #: Whether the charge includes a discount
    is_discounted = False

    def calculate(self, basket):
        """
        Return the shipping charge for the given basket
        """
        raise NotImplemented()

    def discount(self, basket):
        """
        Return the discount on the standard shipping charge
        """
        # The regular shipping methods don't add a default discount.
        # For offers and vouchers, the discount will be provided
        # by a wrapper that Repository.apply_shipping_offer() adds.
        return D('0.00')


class Free(Base):
    """
    This shipping method specifies that shipping is free.
    """
    code = 'free-shipping'
    name = _('Free shipping')
    description = "Disponible à Comores en Ligne à Moroni Caltex"

    def calculate(self, basket):
        # If the charge is free then tax must be free (musn't it?) and so we
        # immediately set the tax to zero
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), tax=D('0.00'))



        
        
        
class NoShippingRequired(Free):
    """
    This is a special shipping method that indicates that no shipping is
    actually required (eg for digital goods).
    """
    code = 'no-shipping-required'
    name = _('Crédit de communication')
    description = "Le crédit sera disponible dans 30 min au maximum"


class FixedPrice(Base):
    """
    This shipping method indicates that shipping costs a fixed price and
    requires no special calculation.
    """
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile')
    description = "Livré à domicile sous 48h au maximum"
    
    # Charges can be either declared by subclassing and overriding the
    # class attributes or by passing them to the constructor
    charge_excl_tax = D('5.35')
    charge_incl_tax =D('6.25')

    def __init__(self, charge_excl_tax=None, charge_incl_tax=None):
        if charge_excl_tax is not None:
            self.charge_excl_tax = charge_excl_tax
        if charge_incl_tax is not None:
            self.charge_incl_tax = charge_incl_tax

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax,
            incl_tax=self.charge_incl_tax)


class Moroni(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Moroni Ville')
    description = "Livré à domicile  -  Moroni en 24h ouvrées"

    charge_excl_tax = D('1.50')
    charge_incl_tax =D('1.50')

class Bambao(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Bambao Ngazidja')
    description = "Livré à domicile  -  Region Bambao Ngazidja en 48h"

    charge_excl_tax = D('2.15')
    charge_incl_tax =D('2.15')

class BadjiniOuest(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Badjini Ouest')
    description = "Livré à domicile  - Region Badjini Ouest en 48h ouvrées"

    charge_excl_tax = D('4.25')
    charge_incl_tax =D('4.25')


class BadjiniEst(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Badjini EST')
    description = "Livré à domicile  - Badjini EST en 48h ouvrées"

    charge_excl_tax = D('4.75')
    charge_incl_tax =D('4.75')


class Hambou(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Hambou')
    description = "Livré à domicile  - Region Hambou en 48h ouvrées"

    charge_excl_tax = D('3.00')
    charge_incl_tax =D('3.00')

class Hamahamet(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Hamahamet')
    description = "Livré à domicile  - Hamahamet en 48h ouvrées"

    charge_excl_tax = D('4.25')
    charge_incl_tax =D('4.25')

class OichiliNgazidja(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Oichili')
    description = "Livré à domicile  - Region Oichili en 48h ouvrées"

    charge_excl_tax = D('4.25')
    charge_incl_tax =D('4.25')

class Mitsamihuli(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Mitsamihuli')
    description = "Livré à domicile  - Region Mitsamihuli en 48h ouvrées"

    charge_excl_tax = D('4.10')
    charge_incl_tax =D('4.10')


class Itsandra(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Itsandra')
    description = "Livré à domicile  -Region Itsandra en 48h ouvrées"

    charge_excl_tax =D('2.75')
    charge_incl_tax =D('2.75')

class MutsamuduAnjouan(FixedPrice):
    code = 'fixed-price-shipping'
    name = _('Livraison à Domicile - Mutsamudu - Ouani')
    description = "Livré à domicile  - region Mutsamudu - Ouani en 24h ouvrées"

    charge_excl_tax = D('1.50')
    charge_incl_tax =D('1.50')





class OfferDiscount(Base):
    """
    Wrapper class that applies a discount to an existing shipping
    method's charges.
    """
    is_discounted = True

    def __init__(self, method, offer):
        self.method = method
        self.offer = offer

    # Forwarded properties

    @property
    def code(self):
        return self.method.code

    @property
    def name(self):
        return self.method.name

    @property
    def discount_name(self):
        return self.offer.name

    @property
    def description(self):
        return self.method.description

    def calculate_excl_discount(self, basket):
        return self.method.calculate(basket)


class TaxExclusiveOfferDiscount(OfferDiscount):
    """
    Wrapper class which extends OfferDiscount to be exclusive of tax.
    """

    def calculate(self, basket):
        base_charge = self.method.calculate(basket)
        discount = self.offer.shipping_discount(base_charge.excl_tax)
        excl_tax = base_charge.excl_tax - discount
        return prices.Price(
            currency=base_charge.currency,
            excl_tax=excl_tax)

    def discount(self, basket):
        base_charge = self.method.calculate(basket)
        return self.offer.shipping_discount(base_charge.excl_tax)


class TaxInclusiveOfferDiscount(OfferDiscount):
    """
    Wrapper class which extends OfferDiscount to be inclusive of tax.
    """

    def calculate(self, basket):
        base_charge = self.method.calculate(basket)
        discount = self.offer.shipping_discount(base_charge.incl_tax)
        incl_tax = base_charge.incl_tax - discount
        excl_tax = self.calculate_excl_tax(base_charge, incl_tax)
        return prices.Price(
            currency=base_charge.currency,
            excl_tax=excl_tax, incl_tax=incl_tax)

    def calculate_excl_tax(self, base_charge, incl_tax):
        """
        Return the charge excluding tax (but including discount).
        """
        if incl_tax == D('0.00'):
            return D('0.00')
        # We assume we can linearly scale down the excl tax price before
        # discount.
        excl_tax = base_charge.excl_tax * (
            incl_tax / base_charge.incl_tax)
        return excl_tax.quantize(D('0.01'))

    def discount(self, basket):
        base_charge = self.method.calculate(basket)
        return self.offer.shipping_discount(base_charge.incl_tax)
