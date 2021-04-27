from django import template
from django.template.defaultfilters import register


@register.filter(is_safe=True)
def concat_address(value, address):
    return str(address) + str(value)