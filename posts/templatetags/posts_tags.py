from django import template
from ..models import Post
from taggit.models import Tag

register = template.Library()

@register.assignment_tag(takes_context=True)
def ultimos(count=6):
	return Post.objects.all().order_by('-fecha')[count:]

@register.inclusion_tag('tags/todos_tags.html')
def todos_tags():
	tags = Tag.objects.all()
	return {'tags':tags}