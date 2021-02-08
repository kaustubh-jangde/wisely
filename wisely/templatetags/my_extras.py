from django import template

register = template.Library()


@register.filter(name='concat')
def concat(value, arg):
    return arg+str(value)
