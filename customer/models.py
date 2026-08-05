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
        if self.discount > price:
            self.discount = price
        self.total_price=price - self.discount
        
        if self.product.stock >= self.quantity:
            self.product.stock -= self.quantity
            self.product.save()
        else:
            from rest_framework.exceptions import ValidationError
            raise ValidationError({"quantity": f"Not enough stock. Only {self.product.stock} left."})
    
        super().save(*args, **kwargs)
    

class Sale(models.Model):
    products=models.ManyToManyField(ProductSold)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)



