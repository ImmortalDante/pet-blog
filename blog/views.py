from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "blog/home.html", context)


def category(request, category_slug):
    context = {
        "category_slug": category_slug,
    }
    return render(request, "blog/category.html", context)


def post(request, post_slug):
    context = {
        "post_slug": post_slug,
    }
    return render(request, "blog/post.html", context)


def search(request, search_request):
    context = {
        "search_request": search_request
    }
    return render(request, "blog/search_result.html", context)
