"""
create custom filter for django templates
"""
from django import template

register = template.Library()


@register.filter(name="special_replace")
def cut_(value, args):
    """ """
    return value.replace(args, "")
