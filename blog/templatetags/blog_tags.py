from django import template

from blog.models import Category, Post


register = template.Library()


@register.simple_tag()
def get_posts(category_slug=None):
    if not category_slug:
        return Post.objects.all()[:2]
    category = get_categories(category_slug=category_slug)
    return Post.objects.filter(category_id=category.pk).all()


@register.simple_tag()
def get_categories(category_slug=None):
    if not category_slug:
        return Category.objects.all()
    return Category.objects.filter(slug=category_slug).first()
