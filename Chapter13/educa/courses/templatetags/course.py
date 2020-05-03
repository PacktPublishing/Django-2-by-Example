from django import template

register = template.Library()

# filter to get name of a model
# object|model_name
@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None
