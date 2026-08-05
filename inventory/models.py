from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=300)
    stock=models.PositiveIntegerField(default=0)
    is_avaliable=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.stock > 0:
            self.is_avaliable = True
        else:
            self.is_avaliable = False

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_name} of {self.category.name}"

