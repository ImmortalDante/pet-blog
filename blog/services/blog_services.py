from blog.models import Category


def get_current_category(category_slug):
    return Category.objects.filter(slug=category_slug).first()
