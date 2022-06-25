from django.urls import path
from admin_users.views import AdminProductList, AdminProductDetail

urlpatterns = [
path('admin-list-product/',AdminProductList.as_view(), name='admin_list_product'),
path('admin-product-detail/<str:pk>/', AdminProductDetail.as_view(), name='admin_product_detail'),
]
