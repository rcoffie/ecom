from django.shortcuts import render
from product.models import Product , Category , Cart
from product.serializers import  CartSerializer, CategorySerializer, ProductSerializer
from rest_framework import generics
# Create your views here.







class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
