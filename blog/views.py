from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category


class BlogHome(ListView):
    model = Category
    template_name = "blog/home.html"
    context_object_name = "categories"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()[:2]
        context["title"] = "Home"
        return context

    def get_queryset(self):
        return Category.objects.all()[:4]


class CategoryToPostView(ListView):
    model = Post
    template_name = "blog/category.html"
    context_object_name = "posts"
    # allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[:4]
        category_obj = Category.objects.filter(slug=self.kwargs["category_slug"]).first()
        context["title"] = category_obj.title
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs["category_slug"]).all()


class PostView(DetailView):
    model = Post
    template_name = "blog/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"


def search(request, search_request):
    context = {
        "search_request": search_request
    }
    return render(request, "blog/search_result.html", context)
