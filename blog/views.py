from django.shortcuts import render

from .services.blog_services import get_current_category


def home(request):
    context = {}
    return render(request, "blog/home.html", context)


def category(request, category_slug):
    context = {
        "category_slug": category_slug,
        "current_category": get_current_category(category_slug),
    }
    return render(request, "blog/category.html", context)


def post_by_category(request, category_slug):
    context = {
        "category_slug": category_slug,
    }
    return render(request, "blog/posts_by_category.html", context)
