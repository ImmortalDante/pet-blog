from django.urls import path
# from django.views.decorators.cache import cache_page

from .views import PostView, BlogHome, CategoryToPostView, RegisterUser, LoginUser, logout_user, search

urlpatterns = [
    # path("", cache_page(60)(BlogHome.as_view()), name="home"),
    # path("category/<slug:category_slug>/", cache_page(60)(CategoryToPostView.as_view()), name="category"),
    path("", BlogHome.as_view(), name="home"),
    path("category/<slug:category_slug>/", CategoryToPostView.as_view(), name="category"),
    path("post/<slug:post_slug>/", PostView.as_view(), name="post"),
    path("subscribe/", RegisterUser.as_view(), name="subscribe"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("search/", search, name="search")
]
