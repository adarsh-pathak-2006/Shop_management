from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from customer.models import Sale, ProductSold
from inventory.serializers import ProductSerializer
from inventory.models import Product

class ProductSoldGetSerializer(ModelSerializer):
    product=ProductSerializer(read_only=True)
    class Meta:
        model=ProductSold
        fields='__all__'

class ProductSoldUpdateSerializer(ModelSerializer):
    product=PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model=ProductSold
        fields='__all__'

class SaleSerializers(ModelSerializer):
    products=ProductSoldGetSerializer(read_only=True, many=True)
    class Meta:
        model=Sale
        fields='__all__'