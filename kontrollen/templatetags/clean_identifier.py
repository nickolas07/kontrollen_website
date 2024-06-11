from django import template

register = template.Library()


@register.filter
def clean_identifier(value):
    return value.split('-')[-1]
