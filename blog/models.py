from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to="categories/%Y/%m/%d/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Categories"
        ordering = ["id"]


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=255, unique=True, db_index=True)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={
            "post_slug": self.slug,
        })

    class Meta:
        verbose_name = "Posts"
        verbose_name_plural = "Posts"
        ordering = ["time_created"]
