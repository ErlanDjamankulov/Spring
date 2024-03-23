from django.urls import path
from .views import CompanyViewSets, ProductViewSets

urlpatterns = [
         path('company/', CompanyViewSets.as_view({'get': 'list', 'post': 'create'}),
                name='company_list'),
         path('company/<int:pk>/', CompanyViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
                name='company_detail'),
         path('product/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}),
                name='product_list'),
         path('product/<int:pk>/', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
                name='product_detail'),
]