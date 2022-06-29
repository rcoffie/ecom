from django.urls import path

from product.views import CartDetail, CartList, CategoryList, ProductDetail, ProductList

urlpatterns = [
    path("product-list/", ProductList.as_view(), name="product_list/"),
    path("category-list/", CategoryList.as_view(), name="cartgory_list"),
    path("cart-list/", CartList.as_view(), name="cart_list"),
    path("product-detail/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("cart-detail/<str:pk>/", CartDetail.as_view(), name="cart_detail"),
]
