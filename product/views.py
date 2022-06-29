from django.shortcuts import render
from product.models import Product , Category , Cart
from product.serializers import  CartSerializer, CategorySerializer, ProductSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from product.pagination import ProductPagination
from product.permissions import CartOwner
from rest_framework.decorators import permission_classes
# Create your views here.







class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['category','name']
    pagination_class = ProductPagination


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    persissions_classes = [CartOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        return Cart.objects.filter(user=user)




class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    persissions_classes = [CartOwner]
