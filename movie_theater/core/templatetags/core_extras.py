from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()
@register.filter('concVar')
@stringfilter
def concVar(arg, var):
	"""
	usage example {{ your_dict|get_value_from_dict:your_key }}
	"""
	return arg+str(var)