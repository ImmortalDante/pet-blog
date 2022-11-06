from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("", kwargs={"slug": self.slug})

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

    def _get_category_slug(self):
        category = Category.objects.get(self.category)
        return category.slug

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("", kwargs={
            "category_slug": self._get_category_slug,
            "post_slug": self.slug,
        })

    class Meta:
        verbose_name = "Posts"
        verbose_name_plural = "Posts"
