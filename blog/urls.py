from django.urls import path

from .views import home, category, post

urlpatterns = [
    path("", home, name="home"),
    path("category/<slug:category_slug>/", category, name="category"),
    path("post/<slug:post_slug>/", post, name="post"),
]
