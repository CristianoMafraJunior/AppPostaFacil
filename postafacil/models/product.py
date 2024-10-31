from django.db import models
from .client import Client


class Product(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.name
