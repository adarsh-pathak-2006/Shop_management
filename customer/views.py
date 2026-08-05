from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from customer.models import Sale, ProductSold
from customer.serializers import ProductSoldGetSerializer, ProductSoldUpdateSerializer, SaleSerializers, SaleWriteSerializer
from django.core.cache import cache
from rest_framework.response import Response
from utsav.throttling import CoreThrottle


class ProductSoldAPI(APIView):
    throttle_classes=[CoreThrottle]
    def get(self, request):
        cached_data=cache.get("productsold")
        if cached_data:
            return Response(cached_data, status=200)
        data=ProductSold.objects.all()
        serial=ProductSoldGetSerializer(data, many=True)
        cache.set("productsold", serial.data, timeout=300)
        return Response(serial.data, status=200)

    def post(self, request):
        serial=ProductSoldUpdateSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            cache.delete("productsold")
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)

class ProductSoldIndividualAPI(APIView):
    throttle_classes=[CoreThrottle]
    def get(self, request, pk):
        cached_data=cache.get(f"productsold_{pk}")
        if cached_data:
            return Response(cached_data, status=200)
        data=get_object_or_404(ProductSold, id=pk)
        serial=ProductSoldGetSerializer(data)
        cache.set(f"productsold_{pk}", serial.data, timeout=300)
        return Response(serial.data, status=200)

    def put(self, request, pk):
        instance=get_object_or_404(ProductSold, id=pk)
        serial=ProductSoldUpdateSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            cache.delete(f"productsold_{pk}")
            cache.delete("productsold")
            serial.save()
            return Response(serial.data, status=200)
        return Response(serial.errors, status=400)

    def delete(self, request, pk):
        data=get_object_or_404(ProductSold, id=pk)
        cache.delete(f"productsold_{pk}")
        cache.delete("productsold")
        data.delete()
        return Response(status=204)

class SaleAPI(APIView):
    throttle_classes=[CoreThrottle]
    def get(self, request):
        cached_data=cache.get("sale")
        if cached_data:
            return Response(cached_data, status=200)
        data=Sale.objects.all()
        serial=SaleSerializers(data, many=True)
        cache.set("sale", serial.data, timeout=300)
        return Response(serial.data, status=200)

    def post(self, request):
        serial=SaleWriteSerializer(data=request.data)
        if serial.is_valid():
            cache.delete("sale")
            serial.save()
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)

class SaleIndividualAPI(APIView):
    throttle_classes=[CoreThrottle]
    def get(self, request, pk):
        cached_data=cache.get(f"sale_{pk}")
        if cached_data is not None:
            return Response(cached_data, status=200)
        data=get_object_or_404(Sale, id=pk)
        serial=SaleWriteSerializer(data)
        cache.set(f"sale_{pk}", serial.data, timeout=300)
        return Response(serial.data, status=200)

    def put(self, request, pk):
        instance=get_object_or_404(Sale, id=pk)
        serial=SaleWriteSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            cache.delete(f"sale_{pk}")
            cache.delete(f"sale")
            serial.save()
            return Response(serial.data, status=200)
        return Response(serial.errors, status=400)

    def delete(self, request, pk):
        data=get_object_or_404(Sale, id=pk)
        cache.delete("sale")
        cache.delete(f"sale_{pk}")
        data.delete()
        return Response(status=204)