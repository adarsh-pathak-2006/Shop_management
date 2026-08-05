from rest_framework.serializers import ModelSerializer
from inventory.models import Product, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSerializer(ModelSerializer):
    category=CategorySerializer(read_only=True)
    class Meta:
        model=Product
        fields='__all__'