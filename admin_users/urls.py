from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from admin_users.views import (
    AdminProductDetail,
    AdminProductList,
    AdminUserCategory,
    UserCreate,
)

urlpatterns = [
    path("admin-list-product/", AdminProductList.as_view(), name="admin_list_product"),
    path(
        "admin-product-detail/<str:pk>/",
        AdminProductDetail.as_view(),
        name="admin_product_detail",
    ),
    path("register/", UserCreate.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path(
        "admin-user-category/<str:pk>/",
        AdminUserCategory.as_view(),
        name="admin_user_category",
    ),
]
