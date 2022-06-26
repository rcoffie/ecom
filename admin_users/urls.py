from django.urls import path
from admin_users.views import AdminProductList, AdminProductDetail, UserCreate
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
path('admin-list-product/',AdminProductList.as_view(), name='admin_list_product'),
path('admin-product-detail/<str:pk>/', AdminProductDetail.as_view(), name='admin_product_detail'),
path('register/', UserCreate.as_view(), name='register'),
path('login/',obtain_auth_token, name='login')
]
