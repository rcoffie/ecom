from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 10

class AdminPagination(PageNumberPagination):
    page_size = 10 
