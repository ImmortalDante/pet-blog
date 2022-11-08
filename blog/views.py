from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "blog/home.html", context)


def category(request, category_slug):
    context = {
        "category_slug": category_slug,
    }
    return render(request, "blog/category.html", context)


def post_by_category():
    pass
