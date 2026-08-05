from django.urls import path
from inventory.views import CategoryAPI, CategoryIndividualAPI, ProductAPI, ProductIndividualAPI

urlpatterns = [
    path('category/', CategoryAPI.as_view(), name='category'),
    path('category/<id:pk>/', CategoryIndividualAPI.as_view(), name='category_individual'),
    path('product/', ProductAPI.as_view(), name='product'),
    path('product/<int:pk>/', ProductIndividualAPI.as_view(), name='product_individual')
]
