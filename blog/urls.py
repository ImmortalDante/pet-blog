from django.urls import path

from .views import PostView, BlogHome, CategoryToPostView, RegisterUser, LoginUser

urlpatterns = [
    path("", BlogHome.as_view(), name="home"),
    path("category/<slug:category_slug>/", CategoryToPostView.as_view(), name="category"),
    path("post/<slug:post_slug>/", PostView.as_view(), name="post"),
    path("subscribe/", RegisterUser.as_view(), name="subscribe"),
    path("login/", LoginUser.as_view(), name="login"),
]
