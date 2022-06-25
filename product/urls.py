from django.urls import path
from product.views import ( ProductList, CartList, CategoryList)

urlpatterns = [

    path('product-list/', ProductList.as_view(),name='product_list/'),
    path('category-list/', CategoryList.as_view(), name='cartgory_list'),
    path('cart-list/',CartList.as_view(), name='cart_list'),

]
