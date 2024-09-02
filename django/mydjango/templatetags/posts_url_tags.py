from django import template

from ..models import Posting


register = template.Library()

@register.simple_tag()
def get_posts():
    return Posting.objects.all()