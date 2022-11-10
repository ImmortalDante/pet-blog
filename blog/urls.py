from django.urls import path

from .views import PostView, BlogHome, CategoryToPostView

urlpatterns = [
    path("", BlogHome.as_view(), name="home"),
    path("category/<slug:category_slug>/", CategoryToPostView.as_view(), name="category"),
    path("post/<slug:post_slug>/", PostView.as_view(), name="post"),
]
