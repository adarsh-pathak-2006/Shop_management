from rest_framework.serializers import ModelSerializer
from customer.models import Sale

class SaleSerializers(ModelSerializer):
    class Meta:
        model=Sale
        fields=['']