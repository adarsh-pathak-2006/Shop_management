from django.shortcuts import get_object_or_404
from inventory.models import Category, Product
from inventory.serializers import CategorySerializer, ProductSerializer, ProductWriteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from utsav.throttling import CoreThrottle


class CategoryAPI(APIView):
    throttle_classes=[CoreThrottle]
    def get(self, request):
        cached_data=cache.get("category")
        if cached_data:
            return Response(cached_data, status=200)
        data=Category.objects.all()
        serial=CategorySerializer(data, many=True)
        cache.set("category", serial.data, timeout=300)
        return Response(serial.data, status=200)

    def post(self, request):
        serial=CategorySerializer(data=request.data)
        if serial.is_valid():
            cache.delete("category")
            serial.save()
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)

class CategoryIndividualAPI(APIView):
    throttle_classes=[CoreThrottle]
    def get(self, request, pk):
        cached_data=cache.get(f"category_{pk}")
        if cached_data:
            return Response(cached_data, status=200)
        data=get_object_or_404(Category, id=pk)
        serial=CategorySerializer(data)
        cache.set(f"category_{pk}", serial.data, timeout=300)
        return Response(serial.data, status=200)

    def put(self, request, pk):
        instance=get_object_or_404(Category, id=pk)
        serial=CategorySerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            cache.delete(f"category_{pk}")
            cache.delete("category")
            serial.save()
            return Response(serial.data, request=200)
        return Response(serial.errors, status=400)

    def delete(self, request, pk):
        data=get_object_or_404(Category, id=pk)
        cache.delete(f"category_{pk}", status=204)
        cache.delete("category")
        data.delete()
        return Response({'message':'data deleted'}, status=204)


class ProductAPI(APIView):
    throttle_classes=[CoreThrottle]
    def get(self, request):
        cached_data=cache.get("product")
        if cached_data:
            return Response(cached_data, status=200)
        data=Product.objects.all()
        serial=ProductSerializer(data, many=True)
        cache.set("product", serial.data, timeout=300)
        return Response(serial.data, status=200)

    def post(self, request):
        serial=ProductWriteSerializer(data=request.data)
        if serial.is_valid():
            cache.delete("product")
            serial.save()
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)

class ProductIndividualAPI(APIView):
    throttle_classes=[CoreThrottle]
    def get(self, request, pk):
        cached_data=cache.get(f"product_{pk}")
        if cached_data:
            return Response(cached_data, status=200)
        data=get_object_or_404(Product, id=pk)
        serial=ProductSerializer(data)
        cache.set(f"product_{pk}", serial.data, timeout=300)
        return Response(serial.data, status=200)

    def put(self, request, pk):
        instance=get_object_or_404(Product, id=pk)
        serial=ProductWriteSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            cache.delete(f"product_{pk}")
            cache.delete("product")
            serial.save()
            return Response(serial.data, status=200)
        return Response(serial.errors, status=400)

    def delete(self, request, pk):
        data=get_object_or_404(Product, id=pk)
        cache.delete(f"product_{pk}")
        cache.delete("product")
        data.delete()
        return Response({'message':'data deleted'}, status=204)
        