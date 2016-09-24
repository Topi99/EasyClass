from django import template
from ..models import Post

register = template.Library()

@register.assignment_tag(takes_context=True)
def ultimos(count=6):
	return Post.objects.all().order_by('-fecha')[count:]