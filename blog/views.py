from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category
from .utils import DataMixin


class BlogHome(DataMixin, ListView):
    model = Category
    template_name = "blog/home.html"
    context_object_name = "categories"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title="Home", posts=Post.objects.all()[:2])
        return dict(list(context.items()) + list(user_context.items()))

    def get_queryset(self):
        return Category.objects.all()


class CategoryToPostView(DataMixin, ListView):
    paginate_by = 4
    model = Post
    template_name = "blog/category.html"
    context_object_name = "posts"
    # allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_obj = Category.objects.filter(slug=self.kwargs["category_slug"]).first().title
        user_context = self.get_user_context(title=category_obj, categories=Category.objects.all())
        return dict(list(context.items()) + list(user_context.items()))

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs["category_slug"]).all()


class PostView(DataMixin, DetailView):
    model = Post
    template_name = "blog/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(categories=Category.objects.all())
        return dict(list(context.items()) + list(user_context.items()))


def search(request, search_request):
    context = {
        "search_request": search_request
    }
    return render(request, "blog/search_result.html", context)
