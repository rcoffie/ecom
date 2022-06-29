import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

current_datetime = datetime.datetime.now()


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    price = models.IntegerField()
    stock = models.IntegerField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.cart_id

    def save(self, *args, **kwargs):
        self.cart_id = slugify("GH" + str(current_datetime))
        super(Cart, self).save(*args, **kwargs)
