from django.shortcuts import render
from rest_framework.views import APIView
from customer.models import Sale, ProductSold
from customer.serializers import ProductSoldGetSerializer, ProductSoldUpdateSerializer, SaleSerializers


