from django.shortcuts import render
from django.contrib.auth.models import User
from product.serializers import ProductSerializer, CartSerializer, CategorySerializer
from product.models import Category, Cart, Product
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.models import User
from admin_users.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import AdminPagination
# Create your views here.


class AdminProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['category','name']
    pagination_class = AdminPagination


class AdminProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AdminUserCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
