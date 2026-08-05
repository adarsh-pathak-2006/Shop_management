from django.db import models
from inventory.models import Product

class ProductSold(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price_per_piece=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    total_price=models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        price=self.price_per_piece * self.quantity
        self.total_price=price - self.discount
    
        super().save(*args, **kwargs)
    

class Sale(models.Model):
    products=models.ManyToManyField(ProductSold)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date



