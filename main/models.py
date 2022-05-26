from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.title
