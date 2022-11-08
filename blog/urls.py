from django.urls import path

from .views import home, category  # , post_by_category

urlpatterns = [
    path("", home, name="home"),
    path("category/<slug:category_slug>/", category, name="category"),
    # path("category/<slug:category_slug>/<slug:post_slug>/", post_by_category, name="post-by-category"),
]
