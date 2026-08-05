from django.contrib import admin
from customer.models import Sale, ProductSold

admin.site.register(ProductSold)
admin.site.register(Sale)
