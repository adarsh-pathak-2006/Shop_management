from django.urls import path
from customer.views import ProductSoldAPI, ProductSoldIndividualAPI, SaleAPI, SaleIndividualAPI

urlpatterns = [
    path('product-sold/', ProductSoldAPI.as_view(), name='product_sold'),
    path('product-sold/<int:pk>/', ProductSoldIndividualAPI.as_view(), name='product_sold_individual'),
    path('sale/', SaleAPI.as_view(), name='sale'),
    path('sale/<int:pk>/', SaleIndividualAPI.as_view(), name='sale_individual'),
]
