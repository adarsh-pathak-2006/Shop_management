from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from customer.models import Sale, ProductSold
from customer.serializers import ProductSoldGetSerializer, ProductSoldUpdateSerializer, SaleSerializers, SaleWriteSerializer
from django.core.cache import cache
from rest_framework.response import Response


class ProductSoldAPI(APIView):
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
            cache.set("productsold", serial.data, timeout=300)
            serial.save()
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)

class ProductSoldIndividualAPI(APIView):
    def get(self, request, pk):
        cached_data=cache.get(f"productsold_{pk}")
        if cached_data:
            return Response(cached_data, status=200)
        data=get_object_or_404(ProductSold, id=pk)
        serial=ProductSoldGetSerializer(data)
        cache.set(f"productsold_{pk}", serial, timeout=300)
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
        return Response({'message':'data deleted'}, status=204)

class SaleAPI(APIView):
    def get(self, request):
        cached_data=cache.get("sale")
        if cached_data:
            return Response(cached_data, status=200)
        data=Sale.objects.all()
        serial=SaleSerializers(data, many=True)
        return Response(serial.data, status=200)

    def post(self, request):
        serial=SaleWriteSerializer(data=request.data)
        if serial.is_valid():
            cache.set("sale", serial.data, timeout=300)
            serial.save()
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)
