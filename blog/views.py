from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView

from .models import Post, Category
from .utils import DataMixin
from .forms import UserRegistrationForm, UserLoginForm


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


class RegisterUser(DataMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = "blog/subscribe.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title="Subscribe")
        return dict(list(context.items()) + list(user_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class LoginUser(DataMixin, LoginView):
    form_class = UserLoginForm
    template_name = "blog/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        user_context = self.get_user_context(title="Login")
        return dict(list(context.items()) + list(user_context.items()))

    def get_success_url(self):
        return reverse_lazy("home")


def search(request):
    search_request = request.POST["search_request"]
    posts = Post.objects.filter(body__contains=search_request).all()
    context = {
        "search_request": search_request,
        "posts": posts,
    }
    return render(request, "blog/search_result.html", context)


def logout_user(request):
    logout(request)
    return redirect("home")
