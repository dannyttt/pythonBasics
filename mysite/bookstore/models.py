from django.db import models
from django.db.models.base import Model
from django.db.models import Q, F

# Create your models here.
class Book(models.Model):
    title = models.CharField("title", max_length=50, default="", unique=True)
    price = models.DecimalField("price", max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField(
        "market price", max_digits=7, decimal_places=2, default=0.0
    )
    pub = models.CharField("publisher", max_length=100, default="")
    info = models.CharField("book info", max_length=100, default="")
    is_active = models.BooleanField("display", default=True)

    class Meta:
        db_table = "book"
        verbose_name = "programming book"
        # verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title}"


class Author(models.Model):
    name = models.CharField("name", max_length=11)
    age = models.IntegerField("age", default=1)
    email = models.EmailField("email", null=True)

    class Meta:
        db_table = "author"

    def __str__(self):
        return f"{self.name}_{self.age}_{self.email}"


class Wife(models.Model):
    name = models.CharField("wife", max_length=50)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
