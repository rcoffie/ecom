from django.contrib import admin
from product.models import Product, Cart, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
